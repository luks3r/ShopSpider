from sql_spider.items import ComputerItem
from sql_spider.settings import DATABASE_URL
from sqlalchemy import create_engine
from models import create_session
from models.computer import Computer

class SQLiteWriterPipeline(object):

    def __init__(self) -> None:
        engine = create_engine(DATABASE_URL)
        self.Session = create_session(engine)
        self.items = []

    def process_item(self, item: ComputerItem, spider) -> ComputerItem:
        computer = Computer.from_item(item)
        self.items.append(computer)
        return item
    
    def close_spider(self, spider) -> None:
        with self.Session() as session:
            session.bulk_save_objects(self.items)
            session.commit()