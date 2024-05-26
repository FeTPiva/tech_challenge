from fastapi import FastAPI

from app.adapters.entrypoints import client, product



fast_app = FastAPI()

@fast_app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


fast_app.include_router(client.router)
fast_app.include_router(product.router)



