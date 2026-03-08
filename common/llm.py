from __future__ import annotations

import json
import logging
import re
from abc import ABC, abstractmethod
from enum import Enum

import httpx

from common.config import settings

logger = logging.getLogger(__name__)

CONFIDENTIAL_PATTERNS = [
    re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"),
    re.compile(r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"),
    re.compile(r"\b(?:mot de passe|password|api[_\s]?key|secret|credential)\b", re.IGNORECASE),
    re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b"),
    re.compile(r"\b(?:FCFA|XOF|EUR|USD)\s*[\d,.]+\b", re.IGNORECASE),
]


class DataSensitivity(str, Enum):
    PUBLIC = "public"
    CONFIDENTIAL = "confidential"


class LLMProvider(ABC):
    @abstractmethod
    async def generate(self, prompt: str, system_prompt: str | None = None) -> str: ...

    @abstractmethod
    async def is_available(self) -> bool: ...


class GeminiFlashProvider(LLMProvider):
    def __init__(self, api_key: str) -> None:
        self._api_key = api_key
        self._base_url = "https://generativelanguage.googleapis.com/v1beta"
        self._model = "gemini-2.0-flash"

    async def generate(self, prompt: str, system_prompt: str | None = None) -> str:
        url = f"{self._base_url}/models/{self._model}:generateContent?key={self._api_key}"

        contents = []
        if system_prompt:
            contents.append({"role": "user", "parts": [{"text": system_prompt}]})
            contents.append({"role": "model", "parts": [{"text": "Compris."}]})
        contents.append({"role": "user", "parts": [{"text": prompt}]})

        payload = {"contents": contents}

        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            data = response.json()

        candidates = data.get("candidates", [])
        if not candidates:
            raise ValueError("Gemini returned no candidates")

        return candidates[0]["content"]["parts"][0]["text"]

    async def is_available(self) -> bool:
        if not self._api_key:
            return False
        try:
            url = f"{self._base_url}/models?key={self._api_key}"
            async with httpx.AsyncClient(timeout=10.0) as client:
                resp = await client.get(url)
                return resp.status_code == 200
        except Exception:
            return False


class OllamaProvider(LLMProvider):
    def __init__(self, base_url: str, model: str) -> None:
        self._base_url = base_url.rstrip("/")
        self._model = model

    async def generate(self, prompt: str, system_prompt: str | None = None) -> str:
        url = f"{self._base_url}/api/generate"
        payload: dict = {
            "model": self._model,
            "prompt": prompt,
            "stream": False,
        }
        if system_prompt:
            payload["system"] = system_prompt

        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            data = response.json()

        return data.get("response", "")

    async def is_available(self) -> bool:
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                resp = await client.get(f"{self._base_url}/api/tags")
                if resp.status_code != 200:
                    return False
                tags = resp.json().get("models", [])
                return any(m.get("name", "").startswith(self._model) for m in tags)
        except Exception:
            return False


def classify_sensitivity(text: str) -> DataSensitivity:
    for pattern in CONFIDENTIAL_PATTERNS:
        if pattern.search(text):
            return DataSensitivity.CONFIDENTIAL
    return DataSensitivity.PUBLIC


class LLMRouter:
    def __init__(self) -> None:
        self._gemini: GeminiFlashProvider | None = None
        self._ollama: OllamaProvider | None = None

        if settings.has_gemini:
            self._gemini = GeminiFlashProvider(settings.gemini_api_key)

        self._ollama = OllamaProvider(settings.ollama_url, settings.ollama_model)

    async def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
        sensitivity: DataSensitivity | None = None,
    ) -> str:
        if sensitivity is None:
            sensitivity = classify_sensitivity(prompt)
            if system_prompt:
                sp_sensitivity = classify_sensitivity(system_prompt)
                if sp_sensitivity == DataSensitivity.CONFIDENTIAL:
                    sensitivity = DataSensitivity.CONFIDENTIAL

        provider = await self._select_provider(sensitivity)
        logger.info("LLM routing: sensitivity=%s, provider=%s", sensitivity, type(provider).__name__)

        return await provider.generate(prompt, system_prompt)

    async def _select_provider(self, sensitivity: DataSensitivity) -> LLMProvider:
        if sensitivity == DataSensitivity.CONFIDENTIAL:
            if self._ollama and await self._ollama.is_available():
                return self._ollama
            raise RuntimeError(
                "Confidential data detected but Ollama is not available. "
                "Refusing to send confidential data to external LLM."
            )

        if self._gemini and await self._gemini.is_available():
            return self._gemini

        if self._ollama and await self._ollama.is_available():
            logger.warning("Gemini unavailable, falling back to Ollama for public data")
            return self._ollama

        raise RuntimeError("No LLM provider available (neither Gemini nor Ollama)")

    async def health_check(self) -> dict:
        gemini_ok = self._gemini is not None and await self._gemini.is_available()
        ollama_ok = self._ollama is not None and await self._ollama.is_available()
        return {
            "gemini_flash": {"available": gemini_ok},
            "ollama": {"available": ollama_ok, "model": settings.ollama_model},
        }


llm_router = LLMRouter()
