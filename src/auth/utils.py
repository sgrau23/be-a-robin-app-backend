from src.database import COLLECTIONS
from uuid import uuid4
from src.auth.crypto import get_hashed_password, verify_password


def get_user(data):
    return COLLECTIONS['users_collections']['users'].find_one(
        {'email': data['email']}
    )


def create_user(data):
    # Prepare user object to be inserted
    user = {
        'email': data['email'],
        'fullName': data['fullName'],
        'id': str(uuid4()) if data['type'] == 'application' else data['id'],
        'password': get_hashed_password(data['password']) if data['type'] == 'application' else None,
        'type': data['type']
    }
    # Insert user on DB
    COLLECTIONS['users_collections']['users'].insert_one(user)
    return {
        'email': user['email'],
        'id': user['id']
    }


def verify_user(data):
    user = get_user(data)
    if user is None:
        return user, False
    if data['type'] == 'application':
        if not verify_password(data['password'], user['password']):
            return user, False
    return user, True
