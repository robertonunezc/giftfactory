from pydantic import BaseModel

# Define a Product model
class Product(BaseModel):
    id: int
    name: str
    price: float
