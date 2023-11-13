from typing import Union

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class StoreBase(BaseModel):
    email: str
    name: str


class StoreCreate(StoreBase):
    name: str


class Store(StoreBase):
    id: int
    is_active: bool
    address: str
    items: list[Item] = []

    class Config:
        from_attributes = True
