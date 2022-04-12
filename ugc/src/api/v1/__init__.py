from fastapi import APIRouter

from . import event

router = APIRouter(prefix="/v1")

router.include_router(event.router)
