from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

def math_symbols() -> InlineKeyboardMarkup:
    btns = [
        [
            InlineKeyboardButton(text="+", callback_data="first"),
            InlineKeyboardButton(text="-", callback_data="second")
        ],
        [
            InlineKeyboardButton(text="*", callback_data="third"),
            InlineKeyboardButton(text="/", callback_data="fourth")   
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=btns)