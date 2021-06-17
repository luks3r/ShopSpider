from scrapy import Item, Field

class ComputerItem(Item):
    title = Field(serializer=str)
    price = Field(serializer=float)
    picture = Field(serializer=str)