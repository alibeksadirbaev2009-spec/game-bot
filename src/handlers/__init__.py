from aiogram import Router

from .commands import router as cmd_router
from .callbacks import router as call_router
from .chat_data import router as chat_router
from .states import router as state_router
from .text import router as text_router
routers = Router()

routers.include_routers(cmd_router, call_router, state_router, chat_router, text_router)