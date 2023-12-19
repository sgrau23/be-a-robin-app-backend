from fastapi import APIRouter
from src.database import COLLECTIONS

# Initialize router manager
router = APIRouter()


@router.post("/users/dislikeMarket")
async def dislike_market():
    ...


@router.post("/users/storePreferences")
async def store_preferences():
    ...


@router.post("/users/login")
async def login():
    ...


@router.post("/users/register")
async def register():
    ...
