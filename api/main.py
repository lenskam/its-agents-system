from __future__ import annotations

import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.health import router as health_router
from common.config import settings
from common.db import close_db_pool, init_db_pool

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=getattr(logging, settings.app_log_level.upper(), logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    logger.info("Starting ITS Agents System (env=%s)", settings.app_env)
    await init_db_pool()
    logger.info("Database pool initialized")
    yield
    await close_db_pool()
    logger.info("ITS Agents System shut down")


app = FastAPI(
    title="ITS Agents System",
    description="Multi-Agent AI System for Odoo Operations",
    version="0.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
