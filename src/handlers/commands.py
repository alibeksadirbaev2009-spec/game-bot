from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message, 
    KeyboardButton, 
    ReplyKeyboardMarkup
)

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    u = message.from_user
    k = [
        [
            KeyboardButton(text="Dizimnen o'tiw")
        ],
        [
            KeyboardButton(text="Ja'rdem"),
            KeyboardButton(text="Profil")
        ]
    ]
    mark = ReplyKeyboardMarkup(keyboard=k, resize_keyboard=True)
    await message.answer(f"Sa'lem, {u.first_name}  Iltimas kerekli bo'limdi saylan'!",
                        reply_markup=mark)

@router.message(Command("help"))
async def help(message: Message):
    await message.answer("""
Bot haqqinda!

Bul bot paydalaniwshilardi dizimnen o'ykeriw ushin jaratilg'an.

Dizimnen o'tiw:
1. At kiritesiz
2. Familya kiritesiz
3. Jas kiritesiz
4. Telefon nomer kiritesiz

Profil:
Dizimnen o'tkennen keyin profilin'izdi ko'riwin'iz mu'mkin.

Esletpe:
Mag'liwmatlardi tuwri kiritin'!                                                 
""")

@router.message(F.text == "Ja'rdem")
async def help(message:Message):
    await message.answer("""
Bot haqqinda!

Bul bot paydalaniwshilardi dizimnen o'ykeriw ushin jaratilg'an.

Dizimnen o'tiw:
1. At kiritesiz
2. Familya kiritesiz
3. Jas kiritesiz
4. Telefon nomer kiritesiz

Profil:
Dizimnen o'tkennen keyin profilin'izdi ko'riwin'iz mu'mkin.

Esletpe:
Mag'liwmatlardi tuwri kiritin'!                                                 
""")
    
# @router.message(Command("contact"))
# async def contact(message: Message):
#     btns = [
#         [
#             KeyboardButton(text="Send contact", request_contact=True)
#         ]
#     ]
#     mark = ReplyKeyboardMarkup(keyboard=btns, resize_keyboard=True)
#     await message.answer("Bul contact!", reply_markup=mark)

# @router.message(Command("keyboard"))
# async def keyboard(message: Message):
#     btns = [
#         [
#             KeyboardButton(text="Hello"),
#             KeyboardButton(text="Qalay")
#         ],
#         [
#             KeyboardButton(text="Hola")
#         ]
#     ]
#     mark = ReplyKeyboardMarkup(keyboard=btns, resize_keyboard=True)
#     await message.answer("Bul help!", reply_markup=mark)

# @router.message(Command("removekb"))
# async def remove_keyboard(message: Message):
#     rm_mark = ReplyKeyboardRemove()
#     await message.answer("Bul knopkani joq qiladi!", reply_markup=rm_mark)

# # InlineKeyboard
# @router.message(Command("game"))
# async def inline_keyboard(message: Message):
#     btns = [
#         [
#             InlineKeyboardButton(text="tas", callback_data="tas")
#         ],
#         [
#             InlineKeyboardButton(text="qagaz", callback_data="qagaz")
#         ],
#         [
#             InlineKeyboardButton(text="qayshi", callback_data="qayshi")
#         ]
#     ]
#     mark = InlineKeyboardMarkup(inline_keyboard=btns)
#     await message.answer("Bul inline keyboard!", reply_markup=mark)