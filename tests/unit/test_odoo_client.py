from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from agents.base import ClientConfig


EXAMPLE_YAML_CONTENT = """
client_id: "test_corp"
name: "Test Corporation"
hosting_type: "self_hosted"

odoo:
  url: "https://odoo.test.com"
  database: "test_db"
  username: "admin"
  api_key: "test_key_123"

ssh:
  host: "server.test.com"
  port: 22
  user: "odoo"
  key_path: "~/.ssh/id_rsa"

monitoring:
  cpu_warning: 70
  cpu_critical: 85
  check_interval_minutes: 5

security:
  stale_days: 90
  forbidden_group_combos:
    - ["account.group_account_manager", "purchase.group_purchase_manager"]
"""


class TestClientConfig:
    def test_from_yaml_loads_all_fields(self, tmp_path: Path) -> None:
        yml_file = tmp_path / "test_corp.yml"
        yml_file.write_text(EXAMPLE_YAML_CONTENT)

        config = ClientConfig.from_yaml(yml_file)

        assert config.client_id == "test_corp"
        assert config.name == "Test Corporation"
        assert config.hosting_type == "self_hosted"
        assert config.odoo_url == "https://odoo.test.com"
        assert config.odoo_database == "test_db"
        assert config.odoo_username == "admin"
        assert config.odoo_api_key == "test_key_123"
        assert config.ssh_host == "server.test.com"
        assert config.ssh_port == 22
        assert config.monitoring_cpu_warning == 70
        assert config.monitoring_cpu_critical == 85
        assert config.security_stale_days == 90
        assert config.security_forbidden_group_combos == [
            ["account.group_account_manager", "purchase.group_purchase_manager"]
        ]

    def test_from_yaml_uses_defaults_for_missing_fields(self, tmp_path: Path) -> None:
        minimal_yaml = """
client_id: "minimal"
name: "Minimal Corp"
hosting_type: "odoo_sh"

odoo:
  url: "https://minimal.odoo.com"
  database: "minimal_db"
  username: "admin"
  api_key: "key"
"""
        yml_file = tmp_path / "minimal.yml"
        yml_file.write_text(minimal_yaml)

        config = ClientConfig.from_yaml(yml_file)

        assert config.client_id == "minimal"
        assert config.hosting_type == "odoo_sh"
        assert config.ssh_host == ""
        assert config.monitoring_cpu_warning == 70
        assert config.security_stale_days == 90
        assert config.security_forbidden_group_combos == []
