from http.client import HTTPException

from sqlalchemy.orm import Session

import models
import schemas


def get_store(db: Session, store_id: int):
    return db.query(models.Store).filter(models.Store.id == store_id).first()


def get_store_by_email(db: Session, email: str):
    return db.query(models.Store).filter(models.Store.email == email).first()


def get_stores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Store).offset(skip).limit(limit).all()


def create_store(db: Session, store: schemas.StoreCreate):
    db_store = models.Store(email=store.email, name=store.name)
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store

def update_store_address(db: Session,address: str,store_id: int):
    store = db.query(models.Store).filter(models.Store.id == store_id).first()
    if store:

        store.address = address

        db.commit()
    return store

def delete_store(db:Session,store_id:int):
    store = db.query(models.Store).filter(models.Store.id == store_id).first()
    if store is None:
        raise HTTPException(status_code=404, detail="Store not found")
    db.delete(store)
    db.commit()
    return {"message": "Store deleted"}

def delete_all_stores(db:Session):
    stores = db.query(models.Store)
    for store in stores:
        db.delete(store)
    db.commit()
    return {"message": "All stores deleted"}