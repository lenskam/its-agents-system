from __future__ import annotations

import logging
import httpx

from common.config import settings
from agents.monitoring.checks import CheckResult

logger = logging.getLogger(__name__)

class AlertManager:
    @staticmethod
    async def send_telegram(message: str) -> bool:
        if not settings.has_telegram:
            logger.warning("Telegram not configured, skipping alert: %s", message)
            return False

        url = f"https://api.telegram.org/bot{settings.telegram_bot_token}/sendMessage"
        payload = {
            "chat_id": settings.telegram_chat_id,
            "text": message,
            "parse_mode": "HTML",
        }

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                resp = await client.post(url, json=payload)
                resp.raise_for_status()
            logger.info("Successfully sent Telegram alert")
            return True
        except Exception:
            logger.exception("Failed to send Telegram alert")
            return False

    @staticmethod
    async def alert_on_critical(client_id: str, results: list[CheckResult]) -> None:
        crises = [r for r in results if r.status == "critical"]
        if not crises:
            return

        lines = [f"🚨 <b>CRITICAL ALERTS - {client_id}</b> 🚨", ""]
        for c in crises:
            lines.append(f"• <b>{c.name}</b>: {c.value} ({c.message})")

        msg = "\n".join(lines)
        await AlertManager.send_telegram(msg)
