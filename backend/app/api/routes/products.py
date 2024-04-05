from fastapi import APIRouter, HTTPException
from models import Product


router = APIRouter()
# Create arouter = APIRouter() list to store the products
products = []

# Endpoint to create a new product
@router.post("/")
def create_product(product: Product):

    return {"message": "Product created successfully", "data": product.dict()}

# Endpoint to get all products
@router.get("/")
def get_all_products():
    return products

# Endpoint to get a specific product by ID
@router.get("/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"message": "Product not found"}

# Endpoint to update a product by ID
@router.put("/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for i, product in enumerate(products):
        if product.id == product_id:
            products[i] = updated_product
            return {"message": "Product updated successfully"}
    return {"message": "Product not found"}

# Endpoint to delete a product by ID
@router.delete("/{product_id}")
def delete_product(product_id: int):
    for i, product in enumerate(products):
        if product.id == product_id:
            del products[i]
            return {"message": "Product deleted successfully"}
    return {"message": "Product not found"}