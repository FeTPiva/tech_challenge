from fastapi import FastAPI

from .adapters.entrypoints import client, product, order


fast_app = FastAPI(title="Tech Challenge Fase 1")

@fast_app.get("/health", tags=["Health Check"])
async def root():
    return {"message": "API Live!"}


fast_app.include_router(client.router)
fast_app.include_router(product.router)
fast_app.include_router(order.router)



