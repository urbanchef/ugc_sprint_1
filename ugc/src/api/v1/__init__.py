from fastapi import APIRouter

from . import bookmark, language, rating, view, watched

router = APIRouter(prefix="/v1")

router.include_router(bookmark.router)
router.include_router(language.router)
router.include_router(rating.router)
router.include_router(view.router)
router.include_router(watched.router)
