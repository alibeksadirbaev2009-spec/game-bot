from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

def game() -> InlineKeyboardMarkup:
    btns = [
        [
            InlineKeyboardButton(text="Rock", callback_data="rock"),
            InlineKeyboardButton(text="Paper", callback_data="paper"),
            InlineKeyboardButton(text="Scissor", callback_data="scissor")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=btns)