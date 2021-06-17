
from sql_spider.items import ComputerItem
from models import Base
from sqlalchemy import Column, Integer, String, Unicode, Float

class Computer(Base):

    __tablename__ = "COMPUTERS"

    id = Column("ID", Integer, primary_key=True)
    title = Column("TITLE", Unicode(255), nullable=False)
    price = Column("PRICE", Float, nullable=False)
    picture = Column("PICTURE", String(255))

    def __init__(self, title: str, price: float, picture: str) -> None:
        self.title = title
        self.price = price
        self.picture = picture

    @classmethod
    def from_item(cls, item: ComputerItem) -> "Computer":
        return cls(
            title = item["title"],
            price = item["price"],
            picture = item["picture"]
        )