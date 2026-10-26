from sqlalchemy import Column, Integer, String
from src.models import Base


class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(255), nullable=True)


    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}', description='{self.description}')>"