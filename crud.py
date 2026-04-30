from sqlalchemy.orm import Session
from models import Product


def create_product(db: Session,product):
    db_product = Product(
        name = product.name,
        price= product.price
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product

def get_products(db:Session):
    return db.query(Product).all()

def update_product(db:Session,product_id: int, updated_product):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        return None
    
    product.name = updated_product.name
    product.price = updated_product.price

    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session,product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()


    if not product:
        return None
    db.delete(product)
    db.commit()
    return product


    
    

