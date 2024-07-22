from fastapi import FastAPI

from entrypoints.client import router as client_router
from entrypoints.product import router as product_router
from entrypoints.order import router as order_router
from entrypoints.payment import router as pay_router


fast_app = FastAPI(title="Tech Challenge Fase 2")

@fast_app.get("/health", tags=["Health Check"])
async def root():
    return {"message": "API Live!"}


fast_app.include_router(client_router)
fast_app.include_router(product_router)
fast_app.include_router(order_router)
fast_app.include_router(pay_router)



