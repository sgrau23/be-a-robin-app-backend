from fastapi import APIRouter

router = APIRouter()


@router.get("/products/categories")
async def categories():
    ...


@router.post("/products/createOffer")
async def create_offer():
    ...


@router.post("/products/extendOffer")
async def extend_offer():
    ...


@router.post("/products/removeTemporalOffer")
async def remove_temporal_offer():
    ...


@router.post("/products/removeOffer")
async def remove_offer():
    ...


@router.post("/products/removeHistoricalOffer")
async def remove_historical_offer():
    ...


@router.post("/products/updateOffer")
async def update_offer():
    ...


@router.post("/products/createLastMinute")
async def create_last_minute():
    ...


@router.post("/products/submitLastMinute")
async def submit_last_minute():
    ...


@router.post("/products/extendLastMinute")
async def extend_last_minute():
    ...


@router.post("/products/removeTemporalLastMinute")
async def remove_temporal_last_minute():
    ...


@router.post("/products/removeLastMinute")
async def remove_last_minute():
    ...


@router.post("/products/removeHistoricalLastMinute")
async def remove_historical_last_minute():
    ...


@router.post("/products/updateLastMinute")
async def update_last_minute():
    ...
