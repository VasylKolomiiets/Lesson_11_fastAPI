"""Модуль для збереження 'бізнес-логікі' сутності проекту `films`.

    Тобто клас, який опрацьовує наші фільми.
"""
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
