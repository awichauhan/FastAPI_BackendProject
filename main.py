from fastapi import FastAPI
from models import Product
from database import SessionLocal, engine
import database_models

products = [
              Product(id=1,name = "phone", description= "budget_phone", price =99, quantity=10),
              Product(id = 2,name ="mac", description ="apple_mac",price= 100, quantity= 2)
]

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)  #asking app to create a table in the database of postgres server

@app.get("/")
def great():
    return "Welcome to my Project"

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")  #dynamic value of id
def get_product_by_id(id :int):  #hard coding the parameter type
    for product in products:
        if product.id == id:
            return product
    return "product not found"

@app.post("/product")
def add_product(product : Product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product added succesfully"
    return "Product not found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product removed succesfully"
    return "Product not found"

