from aiogram import F, Router
from aiogram.types import (
    Message
)

router = Router()

@router.message(F.text)
async def text(message: Message):
    text = message.text
    await message.answer(f"Bot ushin bunday comanda tanis emes: {text}")