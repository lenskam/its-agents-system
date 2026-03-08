from __future__ import annotations

from typing import Any

from agents.base import BaseAgent, AgentResult, ClientConfig
from common.odoo_client import OdooClient
from agents.monitoring.checks import (
    CheckResult,
    check_odoo_ping,
    check_odoo_workers,
    check_server_cpu,
    check_server_ram,
    check_server_disk,
)
from agents.monitoring.alerting import AlertManager


class MonitoringAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__(agent_type="monitoring", name="Monitoring Agent")

    async def health_check(self) -> bool:
        return True

    async def execute(self, client_config: ClientConfig, **kwargs: Any) -> AgentResult:
        odoo_client = OdooClient(client_config)
        
        results: list[CheckResult] = []

        # 1. API reachable?
        ping_res = await check_odoo_ping(client_config.client_id, odoo_client)
        results.append(ping_res)

        # 2. Worker / Query check
        if ping_res.status == "ok":
            work_res = await check_odoo_workers(client_config.client_id, odoo_client)
            results.append(work_res)

        # 3. Server checks (if self-hosted)
        results.append(await check_server_cpu(client_config))
        results.append(await check_server_ram(client_config))
        results.append(await check_server_disk(client_config))

        # 4. Process alerts if critical
        await AlertManager.alert_on_critical(client_config.client_id, results)

        # Summary Log
        critical_count = sum(1 for r in results if r.status in ("critical", "error"))
        if critical_count > 0:
            await self.log(
                "WARNING",
                f"Completed monitoring checks with {critical_count} critical/error items.",
                client_id=client_config.client_id,
            )
        else:
            await self.log(
                "INFO",
                "Monitoring checks passed seamlessly.",
                client_id=client_config.client_id,
            )

        return AgentResult(
            success=critical_count == 0,
            data={"checks": [r.model_dump() for r in results]},
        )
