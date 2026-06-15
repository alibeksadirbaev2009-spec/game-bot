from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from src.keyboards.game import game
from src.states.auth import AuthStates, Change_profile
from src.crud.users import UserRepo

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    u = message.from_user                                     
    await message.answer(f"Hello, {u.first_name}. Oyindi baslaw ushin game commandasin kiritin'!")

@router.message(Command("game"))
async def state_game(message: Message):
    btns = game()
    await message.answer(f"Kerekli qoldi saylan'.", reply_markup=btns)
    
@router.message(Command("help"))
async def help(message: Message):
    await message.answer("""
Bot haqqinda!

Bul bot paydalaniwshilardi dizimnen o'tkeriw ushin jaratilg'an.

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

@router.message(Command("register"))
async def sign_in(message: Message, state: FSMContext):
    await state.set_state(AuthStates.name)
    await message.answer("Atin'izdi kiritin':")

@router.message(Command("stats"))
async def get_statistics(message: Message):
    data = await UserRepo.get_statas(message.from_user.id)

    if data.total == 0:
        win_rate = tie_rate = defeat_rate = 0
    else:
        win_rate = (data.point * 100) / data.total
        tie_rate = (data.tie * 100) / data.total
        defeat_rate = (data.defeat * 100) / data.total

    stat_text = f"""
<b>Sizdin' statistikan'iz:</b>

🏆 Utiw: {data.point} | {round(win_rate, 1)}%
🤝 Ten'lik: {data.tie} | {round(tie_rate, 1)}%
💀 Utilis: {data.defeat} | {round(defeat_rate, 1)}%
📊 Uliwma oyinlar sani: {data.total}
"""
    await message.answer(text=stat_text, parse_mode="HTML")

@router.message(Command("profile"))
async def profile(message: Message):
    data = await UserRepo.get_user_by_telegram_id(message.from_user.id)

    if not data:
        await message.answer("Siz dizimnen o'tpegensiz!")
        return

    text = f"""

👤 <b>Profil</b>
🆔 Telegram ID: {data.telegram_id}
👨 At: {data.first_name}
👤 Familiya: {data.lastname}
🎂 Jas: {data.age}
📞 Telefon: {data.phone}
📍 Addres: {data.location}
"""
    await message.answer(text, parse_mode="HTML")

@router.message(Command("change_profile"))
async def change_profil(message: Message, state: FSMContext):
    await state.set_state(Change_profile.name)
    await message.answer(f"Atin'izdi kiritin'!")


# @router.message(Command())
    
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