import asyncio
import logging
from aiogram import Bot, Dispatcher
from .config import settings
from .handlers import routers
from .utils.my_commands import my_commands
from .database.create_models import async_main

bot = Bot(settings.TOKEN)
dp = Dispatcher()

dp.include_routers(routers)


async def main():
    await async_main()
    await bot.set_my_commands(my_commands())
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
    
if __name__ =="__main__":
    asyncio.run(main=main())




# ten'lik, qalesek utilg'an, model oz'gerse boladi, register o'zgertiwgetse boladi, logika game utsa 1 teng 1 total1 1