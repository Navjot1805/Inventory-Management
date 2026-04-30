from fastapi import FastAPI, Depends,HTTPException
from sqlalchemy.orm import Session

import models
import Schemas
import crud

from database import engine, SessionLocal
# create tables
models.Base.metadata.create_all(bind=engine)
#Create all tables defined in models if they don’t exist
app = FastAPI() # intialize API

# dependency connection like DB. (DB Session)


def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()


#routes
@app.post("/product",response_model=Schemas.ProductResponse)
def create_product(product:Schemas.ProductCreate,db:Session=Depends(get_db)):
    return crud.create_product(db,product)

# response model ensures output matches  with productResponse
# product input data validated by pydantic db database injected using Depends(get_db)
    
@app.get("/product",response_model=list[Schemas.ProductResponse]) # fetch all products list
def read_products(db:Session=Depends(get_db)):  # get DB session
    return crud.get_products(db)

@app.put("/product/{product_id}",response_model=Schemas.ProductResponse)
def update_product(
    product_id: int,
    product: Schemas.ProductCreate, #  new product
    db:Session=Depends(get_db)
):
    updated = crud.update_product(db,product_id,product)

    if not updated:
        raise HTTPException(status_code=404,detail="Product not found")
    return updated


@app.delete("/product/{product_id}")
def delete_product(product_id:int,db:Session=Depends(get_db)):
    deleted = crud.delete_product(db,product_id)

    if not deleted:
        raise HTTPException(status_code=404,detail="Product not found")
    
    return {"message":"Product deleted successfully"}
