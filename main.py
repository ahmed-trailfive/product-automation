from fastapi import FastAPI
import uvicorn

from config import settings
from apps.firestore.db import DatabaseInitialize


from apps.product.routers import router as product_router
from apps.user.routers import router as user_router


app = FastAPI(
    title="Product Automation",
    description="Automate the process of posting ads on sprzedajemy.pl",
)


@app.on_event("startup")
async def startup_db_client():
    app.db = DatabaseInitialize()


app.include_router(user_router, tags=["user"], prefix="/user")
app.include_router(product_router, tags=["product"], prefix="/product")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )
