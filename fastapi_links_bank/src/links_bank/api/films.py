"""Модуль для обробки всіх HTTP-roots для '/films' - тобто фільмів."""
from fastapi import APIRouter
from fastapi import Depends

from ..models.films import Film
from ..services.films import FilmsService


router = APIRouter(prefix="/films")


@router.get("/", response_model=list[Film])
def read_films(service: FilmsService = Depends()):
    return service.get_all()
