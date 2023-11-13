from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.exc import IntegrityError

import models
import schemas
import crud
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from pydantic import BaseModel


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class StoreDeleteResponse(BaseModel):
    message: str

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root_get() -> str:
    return "Hello World"


@app.post("/stores/", response_model=schemas.Store)
def create_store(store: schemas.StoreCreate, db: Session = Depends(get_db)):
    """ db_store = crud.get_store_by_email(db, email=store.email)
    print(db_store)
    if db_store:
        raise HTTPException(status_code=400, detail="Email already registered")"""
    try:
        return crud.create_store(db=db, store=store)
    except IntegrityError as e:
        if "email" in repr(e).lower():
            raise HTTPException(status_code=400, detail="Email already registered")
        raise HTTPException(status_code=400, detail=e.detail)



@app.get("/items/", response_model=list[schemas.Store])
async def get_stores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stores = crud.get_stores(db, skip=skip, limit=limit)
    return stores


@app.get("/items", response_model=schemas.Store)
async def get_store_by_email(email: str, db: Session = Depends(get_db)):
    store = crud.get_store_by_email(db, email=email)
    return store


@app.put("/stores/{store_address}", response_model=schemas.Store)
async def update_store_address(new_address: str, id: int,
                               db: Session = Depends(get_db)):
    store = crud.update_store_address(db, new_address, id)
    if store:
        return store
    raise HTTPException(status_code=400, detail="Store ID doesn't exist")


@app.put("/stores/{id}", response_model=StoreDeleteResponse)
async def delete_store(id: int, db: Session = Depends(get_db)):
    return crud.delete_store(db, store_id=id)


@app.put("/stores/", response_model=StoreDeleteResponse)
async def delete_all_stores(db: Session = Depends(get_db)):
    return crud.delete_all_stores(db)