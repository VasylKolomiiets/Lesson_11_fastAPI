"""Модуль для обробки всіх HTTP-roots для '/films' - тобто фільмів."""
from fastapi import APIRouter

router = APIRouter(prefix="/operations")
