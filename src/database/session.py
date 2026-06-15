from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from ..config import settings

engine = create_async_engine(settings.DB_URL, echo=False)

async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)