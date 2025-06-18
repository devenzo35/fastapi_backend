# Import necessary modules

from enum import Enum
from fastapi import FastAPI

# Initialize FastAPI application
app = FastAPI()


# Enum representing available premium products
class PremiumProducts(str, Enum):
    naiki = "naiki"
    reboot = "reboot"
    adaidas = "adaidas"


# Root endpoint returning a welcome message
@app.get("/")
async def root():
    return {"message": "Hello message"}


# Endpoint for retrieving user's products (placed before parameterized route to avoid conflicts)
@app.get("/product/my_product")
async def my_product():
    return {"message": "Here are your products"}


# Endpoint for retrieving information about a specific premium product using Enum
@app.get("/premium/{premium_product}")
async def premium_products(premium_product: PremiumProducts):

    if premium_product is PremiumProducts.naiki:
        return {"message": premium_product}

    if premium_product is PremiumProducts.reboot:
        return {"message": premium_product}

    if premium_product is PremiumProducts.adaidas:
        return {"message": premium_product}

    return {"message": "Product not found"}


# Endpoint that accepts a product ID as a path parameter
@app.get("/product/{product_id}")
async def products(product_id: int):
    return {"message": product_id}


# Simulated stock database
false_stock_db = [
    {"product_name": "low range"},
    {"product_name": "high battery"},
    {"product_name": "sport changer"},
]


# Endpoint for retrieving stock information with optional query parameters for pagination and search
@app.get("/stock/")
async def stock(skip: int = 0, limit: int = 10, q: str | None = None):
    if q:
        return "You used the q query, nice job!"
    return false_stock_db[skip : skip + limit]
