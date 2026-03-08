from __future__ import annotations

import logging
import xmlrpc.client
from typing import Any

from agents.base import ClientConfig

logger = logging.getLogger(__name__)


class OdooClient:
    def __init__(self, config: ClientConfig) -> None:
        self.config = config
        self._uid: int | None = None
        self._common: xmlrpc.client.ServerProxy | None = None
        self._models: xmlrpc.client.ServerProxy | None = None

    def _get_common(self) -> xmlrpc.client.ServerProxy:
        if self._common is None:
            url = f"{self.config.odoo_url}/xmlrpc/2/common"
            self._common = xmlrpc.client.ServerProxy(url, allow_none=True)
        return self._common

    def _get_models(self) -> xmlrpc.client.ServerProxy:
        if self._models is None:
            url = f"{self.config.odoo_url}/xmlrpc/2/object"
            self._models = xmlrpc.client.ServerProxy(url, allow_none=True)
        return self._models

    def authenticate(self) -> int:
        if self._uid is not None:
            return self._uid

        common = self._get_common()
        uid = common.authenticate(
            self.config.odoo_database,
            self.config.odoo_username,
            self.config.odoo_api_key,
            {},
        )
        if not uid:
            raise ConnectionError(
                f"Odoo authentication failed for {self.config.client_id} "
                f"at {self.config.odoo_url}"
            )
        self._uid = uid
        logger.info("Authenticated to Odoo: client=%s, uid=%s", self.config.client_id, uid)
        return uid

    def ping(self) -> bool:
        try:
            common = self._get_common()
            version = common.version()
            return bool(version and version.get("server_version"))
        except Exception:
            logger.exception("Odoo ping failed for %s", self.config.client_id)
            return False

    def search_read(
        self,
        model: str,
        domain: list | None = None,
        fields: list[str] | None = None,
        limit: int | None = None,
        offset: int = 0,
    ) -> list[dict[str, Any]]:
        uid = self.authenticate()
        models = self._get_models()

        kwargs: dict[str, Any] = {}
        if fields:
            kwargs["fields"] = fields
        if limit is not None:
            kwargs["limit"] = limit
        if offset:
            kwargs["offset"] = offset

        return models.execute_kw(
            self.config.odoo_database,
            uid,
            self.config.odoo_api_key,
            model,
            "search_read",
            [domain or []],
            kwargs,
        )

    def search_count(self, model: str, domain: list | None = None) -> int:
        uid = self.authenticate()
        models = self._get_models()
        return models.execute_kw(
            self.config.odoo_database,
            uid,
            self.config.odoo_api_key,
            model,
            "search_count",
            [domain or []],
        )

    def execute(self, model: str, method: str, *args: Any, **kwargs: Any) -> Any:
        uid = self.authenticate()
        models = self._get_models()
        return models.execute_kw(
            self.config.odoo_database,
            uid,
            self.config.odoo_api_key,
            model,
            method,
            list(args),
            kwargs,
        )

    def get_users(self, active_only: bool = True) -> list[dict[str, Any]]:
        domain = [("active", "=", True)] if active_only else []
        return self.search_read(
            "res.users",
            domain=domain,
            fields=["id", "name", "login", "groups_id", "active", "login_date"],
        )

    def get_groups(self) -> list[dict[str, Any]]:
        return self.search_read(
            "res.groups",
            fields=["id", "name", "full_name", "users"],
        )
