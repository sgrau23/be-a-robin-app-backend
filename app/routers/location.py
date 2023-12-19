from fastapi import APIRouter

router = APIRouter()


@router.get("/location/getAddress")
async def get_address():
    ...
