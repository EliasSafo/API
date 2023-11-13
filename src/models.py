from sqlalchemy import Boolean, Column, Integer, String


from database import Base


class Store(Base):
    __tablename__ = "store"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=True)
    address = Column(String, unique=False, index=True, default="")
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
