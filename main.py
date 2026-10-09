from fastapi import FastAPI
from models import Product

product = [
              Product(id=1,name = "phone", description= "budget_phone", price =99, quantity=10),
                Product(id = 2,name ="mac", description ="apple_mac",price= 100, quantity= 2)
]

app = FastAPI()

@app.get("/")
def great():
    return "Welcome to my Project"

@app.get("/products")
def get_all_products():
    return product
