from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from random import randint, choice
from src.keyboards.game import math_symbols
from src.states.auth import AuthStates

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    u = message.from_user
    await message.answer(f"Hello, {u.first_name}. Oyindi baslaw ushin game commandasin kiritin'!")

@router.message(Command("game"))
async def state_game(message: Message, state: FSMContext):
    a = randint(1, 100)
    b = randint(1, 100)

    belgi = choice(["+", "-", "*", "/"])
    
    if belgi == "+":
        answer = a + b
    elif belgi == "-":
        answer = a - b
    elif belgi == "*":
        answer = a * b
    else:
        answer = a / b
    
    btns = math_symbols()
    await state.update_data(belgi = belgi)
    await message.answer(f"""Iltimas o'zin'iz kerekli dep bilgen belgini saylan'!
{a} ? {b} = {answer}""", reply_markup=btns)
    await state.set_state(AuthStates.get_answer)
    
# @router.message(Command("help"))
# async def help(message: Message):
#     await message.answer("""
# Bot haqqinda!

# Bul bot paydalaniwshilardi dizimnen o'ykeriw ushin jaratilg'an.

# Dizimnen o'tiw:
# 1. At kiritesiz
# 2. Familya kiritesiz
# 3. Jas kiritesiz
# 4. Telefon nomer kiritesiz

# Profil:
# Dizimnen o'tkennen keyin profilin'izdi ko'riwin'iz mu'mkin.

# Esletpe:
# Mag'liwmatlardi tuwri kiritin'!                                                 
# """)

# @router.message(F.text == "Ja'rdem")
# async def help(message:Message):
#     await message.answer("""
# Bot haqqinda!

# Bul bot paydalaniwshilardi dizimnen o'ykeriw ushin jaratilg'an.

# Dizimnen o'tiw:
# 1. At kiritesiz
# 2. Familya kiritesiz
# 3. Jas kiritesiz
# 4. Telefon nomer kiritesiz

# Profil:
# Dizimnen o'tkennen keyin profilin'izdi ko'riwin'iz mu'mkin.

# Esletpe:
# Mag'liwmatlardi tuwri kiritin'!                                                 
# """)
    
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