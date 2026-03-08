from __future__ import annotations

from typing import Any
from pydantic import BaseModel

from common.odoo_client import OdooClient
from agents.base import ClientConfig


class CheckResult(BaseModel):
    name: str
    status: str  # "ok", "warning", "critical", "error"
    value: Any
    threshold: Any | None = None
    message: str = ""


async def check_odoo_ping(client_id: str, odoo_client: OdooClient) -> CheckResult:
    is_up = odoo_client.ping()
    status = "ok" if is_up else "critical"
    return CheckResult(
        name="odoo_ping",
        status=status,
        value=is_up,
        message="Odoo is responding" if is_up else "Odoo is down or unreachable",
    )


async def check_odoo_workers(client_id: str, odoo_client: OdooClient) -> CheckResult:
    # Requires an established connection and enough privileges.
    # In a real environment, you might query ir.logging or specific worker models.
    # For MVP, we will try a simple query to see if it responds fast enough.
    try:
        count = odoo_client.search_count("res.users", [])
        return CheckResult(
            name="odoo_workers_responsive",
            status="ok",
            value=count,
            message="Odoo API is responsive",
        )
    except Exception as e:
        return CheckResult(
            name="odoo_workers_responsive",
            status="error",
            value=None,
            message=f"Failed to query Odoo models: {e}",
        )


async def check_server_cpu(client_config: ClientConfig) -> CheckResult:
    if client_config.hosting_type != "self_hosted":
        return CheckResult(
            name="server_cpu",
            status="ok",
            value="N/A",
            message="Skipped (not self-hosted)",
        )
    
    # In a real setup, connect via Paramiko to execute top/vmstat. For MVP, we mock.
    # We would use config values: client_config.ssh_host, etc.
    return CheckResult(
        name="server_cpu",
        status="ok",
        value=45,
        threshold=client_config.monitoring_cpu_warning,
        message="Simulated SSH Check: CPU usage normal",
    )

async def check_server_ram(client_config: ClientConfig) -> CheckResult:
    if client_config.hosting_type != "self_hosted":
        return CheckResult(name="server_ram", status="ok", value="N/A", message="Skipped")
    
    return CheckResult(
        name="server_ram",
        status="ok",
        value=60,
        threshold=client_config.monitoring_ram_warning,
        message="Simulated SSH Check: RAM usage normal",
    )

async def check_server_disk(client_config: ClientConfig) -> CheckResult:
    if client_config.hosting_type != "self_hosted":
        return CheckResult(name="server_disk", status="ok", value="N/A", message="Skipped")
    
    return CheckResult(
        name="server_disk",
        status="ok",
        value=50,
        threshold=client_config.monitoring_disk_warning,
        message="Simulated SSH Check: Disk usage normal",
    )
