from fastapi import APIRouter

router = APIRouter()


@router.get("/lastMinutes/getTotalProducts")
async def get_total_products():
    ...


@router.get("/lastMinutes/getMarketsInfo")
async def get_markets_info():
    ...
