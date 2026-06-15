from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio.session import AsyncAttrs

class Base(DeclarativeBase, AsyncAttrs):
    pass