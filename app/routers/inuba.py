from fastapi import APIRouter

router = APIRouter()


@router.get("/inuba/getIntolerances")
async def get_intolerances():
    ...


@router.get("/inuba/getProducts")
async def get_products():
    ...


@router.get("/inuba/getProductsSuperFamilies")
async def get_products_super_families():
    ...
