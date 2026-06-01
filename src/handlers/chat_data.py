from aiogram import F, Router
from aiogram.types import CallbackQuery
from random import choice

router = Router()

hands = ['tas', 'qagaz', 'qayshi']

@router.callback_query(F.data)
async def callback(call: CallbackQuery):
    user = call.data
    bot = choice(hands)
    if user == bot:
        await call.message.answer(f"Ten'lik")
    else:
        await call.message.answer(f"Ten'lik emes")