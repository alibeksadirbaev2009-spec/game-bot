import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from .config import settings
from .handlers import routers
from .utils.my_commands import my_commands

bot = Bot(settings.TOKEN)
dp = Dispatcher()

dp.include_routers(routers)


async def main():
    await bot.set_my_commands(my_commands())
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
    
if __name__ =="__main__":
    asyncio.run(main=main())
