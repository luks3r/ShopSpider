from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

Base = declarative_base()

def create_session(engine):
    Base.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine))

async def create_async_session(engine, drop=False):
    async with engine.begin() as conn:
        if drop:
            await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    
    return scoped_session(sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    ))
    