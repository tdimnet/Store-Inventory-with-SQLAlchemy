from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///inventory.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    price = Column("Price", Integer)
    quantity = Column("Quantity", Integer)
    date = Column("Date", Date)

    def __repr__(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"