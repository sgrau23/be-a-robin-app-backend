from fastapi import APIRouter, HTTPException, status
from src.auth.schemas import LoginItem, RegisterItem, UserCreatedItem, TokenSchema
from fastapi.encoders import jsonable_encoder
from src.utils import get_settings
from src.auth.utils import get_user, create_user, verify_user
from src.auth.crypto import get_access_tokens


# Initialize router manager
router = APIRouter()

# Load settings
SETTINGS = get_settings('api')


@router.post(
    "/auth/login",
    summary='Create access and refresh tokens for user',
    response_model=TokenSchema
)
async def login(data: LoginItem):
    user, exists = verify_user(jsonable_encoder(data))
    if not exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    return get_access_tokens(user['email'])


@router.post(
    "/auth/register",
    summary='Create new user'
)
async def register(data: RegisterItem):
    # Give json format to data
    data = jsonable_encoder(data)
    # Check if user already exists
    user = get_user(data)
    if (user is not None) and (data['type'] == 'application'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )
    # If user already exists but is from an external app return access tokens
    elif (user is not None) and (data['type'] != 'application'):
        return get_access_tokens(user['email'])
    # Otherwise create a new user
    return create_user(data)
