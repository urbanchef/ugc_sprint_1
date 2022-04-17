from fastapi import APIRouter

from . import event, language

router = APIRouter(prefix="/v1")

router.include_router(event.router)
router.include_router(language.router)
