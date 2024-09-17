"""Виконується завжди першим, коли ми звертаємось до модуля `api`.

   Тут будуть зберігатися всі окремі роутери для подальшого 
   поділення коду на логічні частини. Спочатку буде розділ `films`.
   А далі - буде видно.
"""
from fastapi import APIRouter
from . import films

router = APIRouter()
router.include_router(films.router)
