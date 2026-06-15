from .session import engine
from .base import Base

from src.models import *

async def async_main():
    async with engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)