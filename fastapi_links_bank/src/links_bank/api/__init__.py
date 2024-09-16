from fastapi import APIRouter
from . import films

router = APIRouter()
router.include_router(films.router)
