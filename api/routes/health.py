from __future__ import annotations

from fastapi import APIRouter

from common.config import settings
from common.llm import llm_router

router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check() -> dict:
    llm_status = await llm_router.health_check()

    return {
        "status": "ok",
        "version": "0.1.0",
        "environment": settings.app_env,
        "services": {
            "llm": llm_status,
            "telegram": {"configured": settings.has_telegram},
        },
    }
