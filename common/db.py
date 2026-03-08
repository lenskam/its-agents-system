from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

import asyncpg

from common.config import settings

logger = logging.getLogger(__name__)

_pool: asyncpg.Pool | None = None


async def init_db_pool() -> asyncpg.Pool:
    global _pool
    if _pool is not None:
        return _pool

    dsn = settings.database_url.replace("postgresql+asyncpg://", "postgresql://")
    _pool = await asyncpg.create_pool(dsn, min_size=2, max_size=10)
    logger.info("Database connection pool created")
    return _pool


async def close_db_pool() -> None:
    global _pool
    if _pool is not None:
        await _pool.close()
        _pool = None
        logger.info("Database connection pool closed")


async def get_pool() -> asyncpg.Pool:
    if _pool is None:
        return await init_db_pool()
    return _pool


@asynccontextmanager
async def get_connection() -> AsyncGenerator[asyncpg.Connection, None]:
    pool = await get_pool()
    async with pool.acquire() as conn:
        yield conn


async def log_to_db(
    level: str,
    message: str,
    agent_type: str | None = None,
    client_id: str | None = None,
    metadata: dict | None = None,
) -> None:
    try:
        async with get_connection() as conn:
            await conn.execute(
                """
                INSERT INTO system_logs (level, agent_type, client_id, message, metadata)
                VALUES ($1, $2, $3, $4, $5::jsonb)
                """,
                level,
                agent_type,
                client_id,
                message,
                _to_json(metadata),
            )
    except Exception:
        logger.exception("Failed to write log to database")


def _to_json(data: dict | None) -> str | None:
    if data is None:
        return None
    import json

    return json.dumps(data)
