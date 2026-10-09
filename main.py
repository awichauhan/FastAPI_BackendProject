from fastapi import FastAPI
from models import Product
from database import SessionLocal, engine
import database_models

products = [
              Product(id=1,name = "phone", description= "budget_phone", price =99, quantity=10),
              Product(id = 2,name ="mac", description ="apple_mac",price= 100, quantity= 2)
]

#every time app is started, it should check if DB table is empty and then load the data to the DB
def init_db():
    db = SessionLocal()
    count = db.query(database_models.Product).count  #checking if table is empty
    if count == 0:
        for product in products:  #converting Pydantic model using model_dump(); getting dictionary and then unpack it using **
            db.add(database_models.Product(**product.model_dump())) #product is pydantic (iterator on products) and Product is DB model
        db.commit()

init_db()

#model_dump() is serialization method by which dictionary is returned; to only get key-value pair we need **object.model_dump()

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

