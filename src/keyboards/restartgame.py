from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def restart() -> InlineKeyboardMarkup:
    btns = [
        [
            InlineKeyboardButton(text="Qaytadan oynaw", callback_data="re")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=btns)