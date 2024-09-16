from fastapi import APIRouter

router=APIRouter(prefix='/films')

@router.get('/')
def get_films():
    return {"films": None}
