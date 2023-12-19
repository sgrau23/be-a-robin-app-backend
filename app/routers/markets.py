from fastapi import APIRouter

router = APIRouter()


@router.get("/markets/getAll")
async def get_all():
    ...
