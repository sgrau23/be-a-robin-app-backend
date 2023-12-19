from fastapi import APIRouter

router = APIRouter()


@router.post("/shoppingCart/addProduct")
async def add_product():
    ...


@router.get("/shoppingCart/getAllProducts")
async def get_all_products():
    ...


@router.post("/shoppingCart/changeProductStatus")
async def change_product_status():
    ...


@router.post("/shoppingCart/deleteUserProducts")
async def delete_user_products():
    ...


@router.get("/shoppingCart/getHistoricalList")
async def get_historical_list():
    ...
