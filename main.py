from uvicorn import run
from contextlib import asynccontextmanager
from starlette.applications import Starlette

from app.route.routes import routes
from app.database.databases import database

@asynccontextmanager
async def lifespan(app):
    await database.connect()
    yield
    await database.disconnect()

app = Starlette(debug=True, routes=routes, lifespan=lifespan)

if __name__ == "__main__":
    run('main:app', reload=True, port=5_000)