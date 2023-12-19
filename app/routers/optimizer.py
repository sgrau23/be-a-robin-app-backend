from fastapi import APIRouter

router = APIRouter()


@router.post("/optimizer/storePreferences")
async def store_preferences():
    ...


@router.post("/optimizer/optimize")
async def optimize():
    ...


@router.get("/optimizer/getOptimization")
async def get_optimization():
    ...


@router.get("/optimizer/getAvailableCategories")
async def get_available_categories():
    ...
