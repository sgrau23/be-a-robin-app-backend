from app.routers import products, users, last_minutes, markets, auth
from src.utils import get_settings
from src.database import initialize_db, initialize_collections
from fastapi import FastAPI
import uvicorn

# Instantiate fast api
app = FastAPI()

# Initialize DB and Collections
initialize_db()
initialize_collections()

# Load settings
SETTINGS = get_settings('api')

# Add api routes
app.include_router(users.router)
app.include_router(products.router)
app.include_router(last_minutes.router)
app.include_router(auth.router)
app.include_router(markets.router)


if __name__ == '__main__':
    uvicorn.run("app.main:app", host="0.0.0.0", port=SETTINGS['port'], reload=SETTINGS['dev_mode'])
