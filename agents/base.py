from __future__ import annotations

import logging
import time
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel

from common.config import settings
from common.db import log_to_db
from common.llm import DataSensitivity, LLMRouter, llm_router


logger = logging.getLogger(__name__)


class AgentResult(BaseModel):
    success: bool
    data: dict[str, Any] | None = None
    error: str | None = None
    execution_time_ms: int = 0


class ClientConfig(BaseModel):
    client_id: str
    name: str
    hosting_type: str

    odoo_url: str = ""
    odoo_database: str = ""
    odoo_username: str = ""
    odoo_api_key: str = ""

    ssh_host: str = ""
    ssh_port: int = 22
    ssh_user: str = ""
    ssh_key_path: str = ""

    monitoring_cpu_warning: int = 70
    monitoring_cpu_critical: int = 85
    monitoring_ram_warning: int = 75
    monitoring_ram_critical: int = 90
    monitoring_disk_warning: int = 80
    monitoring_disk_critical: int = 95
    monitoring_check_interval_minutes: int = 5

    security_stale_days: int = 90
    security_forbidden_group_combos: list[list[str]] = []

    @classmethod
    def from_yaml(cls, path: Path) -> ClientConfig:
        with open(path) as f:
            raw = yaml.safe_load(f)

        odoo = raw.get("odoo", {})
        ssh = raw.get("ssh", {})
        mon = raw.get("monitoring", {})
        sec = raw.get("security", {})

        return cls(
            client_id=raw["client_id"],
            name=raw["name"],
            hosting_type=raw["hosting_type"],
            odoo_url=odoo.get("url", ""),
            odoo_database=odoo.get("database", ""),
            odoo_username=odoo.get("username", ""),
            odoo_api_key=odoo.get("api_key", ""),
            ssh_host=ssh.get("host", ""),
            ssh_port=ssh.get("port", 22),
            ssh_user=ssh.get("user", ""),
            ssh_key_path=ssh.get("key_path", ""),
            monitoring_cpu_warning=mon.get("cpu_warning", 70),
            monitoring_cpu_critical=mon.get("cpu_critical", 85),
            monitoring_ram_warning=mon.get("ram_warning", 75),
            monitoring_ram_critical=mon.get("ram_critical", 90),
            monitoring_disk_warning=mon.get("disk_warning", 80),
            monitoring_disk_critical=mon.get("disk_critical", 95),
            monitoring_check_interval_minutes=mon.get("check_interval_minutes", 5),
            security_stale_days=sec.get("stale_days", 90),
            security_forbidden_group_combos=sec.get("forbidden_group_combos", []),
        )


def load_all_clients() -> list[ClientConfig]:
    clients_dir = settings.clients_path
    if not clients_dir.exists():
        logger.warning("Clients config directory not found: %s", clients_dir)
        return []

    configs = []
    for yml_file in sorted(clients_dir.glob("*.yml")):
        if yml_file.name == "example_client.yml":
            continue
        try:
            configs.append(ClientConfig.from_yaml(yml_file))
            logger.info("Loaded client config: %s", yml_file.name)
        except Exception:
            logger.exception("Failed to load client config: %s", yml_file.name)
    return configs


class BaseAgent(ABC):
    def __init__(self, agent_type: str, name: str) -> None:
        self.agent_type = agent_type
        self.name = name
        self._llm = llm_router

    @abstractmethod
    async def execute(self, client_config: ClientConfig, **kwargs: Any) -> AgentResult:
        ...

    @abstractmethod
    async def health_check(self) -> bool:
        ...

    async def llm_generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
        sensitivity: DataSensitivity | None = None,
    ) -> str:
        return await self._llm.generate(prompt, system_prompt, sensitivity)

    async def log(self, level: str, message: str, client_id: str | None = None) -> None:
        logger.log(logging.getLevelName(level.upper()), "[%s] %s", self.name, message)
        await log_to_db(level, message, agent_type=self.agent_type, client_id=client_id)

    async def run(self, client_config: ClientConfig, **kwargs: Any) -> AgentResult:
        start = time.perf_counter()
        await self.log("INFO", f"Starting execution for client {client_config.client_id}")

        try:
            result = await self.execute(client_config, **kwargs)
            elapsed_ms = int((time.perf_counter() - start) * 1000)
            result.execution_time_ms = elapsed_ms
            await self.log(
                "INFO",
                f"Completed in {elapsed_ms}ms (success={result.success})",
                client_id=client_config.client_id,
            )
            return result
        except Exception as exc:
            elapsed_ms = int((time.perf_counter() - start) * 1000)
            await self.log(
                "ERROR",
                f"Failed after {elapsed_ms}ms: {exc}",
                client_id=client_config.client_id,
            )
            return AgentResult(
                success=False,
                error=str(exc),
                execution_time_ms=elapsed_ms,
            )
