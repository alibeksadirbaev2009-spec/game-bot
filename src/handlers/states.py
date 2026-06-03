from  aiogram import Router, F
from aiogram.types import (
    Message, 
    ReplyKeyboardMarkup, 
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
    )
from aiogram.fsm.context import FSMContext
from src.states.auth import AuthStates
from aiogram.filters import Command
import random

router = Router()

@router.message(AuthStates.name)
async def state_name(message: Message, state: FSMContext):
    name = message.text    
    if not name.isalpha():
        await message.answer(f"Atin'ız tek ha'riplerden ibarat bolsın, eshqanday belgilersiz!")
        return
    
    await state.set_data({'name': name})
    await message.answer(f"Atin'izdi qabillandi, endi Familyan'izdi kiritin'.")
    await state.set_state(AuthStates.lastname)

@router.message(AuthStates.lastname)
async def state_lastname(message: Message, state: FSMContext):
    lastname = message.text
    if not lastname.isalpha():
        await message.answer(f"Familya'iz tek ha'riplerden ibarat bolsın, eshqanday belgilersiz!")
        return
    await state.set_data({'lastname': lastname})
    
    await message.answer(f"Familyan'izdi qabillandi, endi jasin'zdi kiritin'.")
    await state.set_state(AuthStates.age)

@router.message(AuthStates.age)
async def state_age(message: Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer(f"Jas tek sanlarda boladi.")
        return
    
    age = int(age)
    if not 10 <= age <= 80:
        await message.answer(f"Jas shegarasi 10 dan baslanip 80 ge shekem!")
        return
    await state.set_data({'age': age})

    await message.answer(f"Jasin'z qabillandi, endi telefon nomerin'izdi kiritin'.")
    await state.set_state(AuthStates.phone)

@router.message(AuthStates.phone)
async def state_phone(message: Message, state: FSMContext):
    phone = message.text

    if not phone.isdigit() or len(phone) !=9:
        await message.answer(f"Telefon nomeri sanlarda boliwi ha'm 9 sannan ibarat boliwi kerek!")
        return
    await state.set_state({'phone': phone})
    await message.answer(f"Telefon nonerin'iz qabillandi, endi manzilin'izdi kritin'.")
    await state.set_state(AuthStates.location)

@router.message(AuthStates.location)
async def state_location(message: Message, state: FSMContext):
    location = message.text 
    
    await state.set_state({'location': location})

    location = [
        [
            KeyboardButton(text="Ma'nzil jiberiw", request_location=True)
        ], 
    ]
    mark = ReplyKeyboardMarkup(keyboard=location, resize_keyboard=True)
    await message.answer("Ma'nzilin'izdi jiberin':", reply_markup=mark)

@router.message(F.location)
async def get_location(message:Message, state: FSMContext):
    await message.answer(f"Ma'zilin'iz qabillandi")
    data = await state.get_data()
    name = data.get('name')
    lastname = data.get('lastname')
    age = data.get('age')
    phone = data.get('phone')
    location = data.get('location')
    await state.clear()
 

@router.message(Command("game"))
async def state_game(message: Message, state: FSMContext):
    await state.set_state(AuthStates.get_answer)
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    belgi = random.choice(["+", "-", "*", "/"])
    challange = random.choice(
        [
        "10 * 10 / 2", 
        "7 * 7 * 10", 
        "11 / 11 *0", 
        "100 / 1000 *10",
        "9 * 9 + 1",
        "8 * 8 - 8",
        "6 * 6 * 2",
        "12 * 12 / 3",
        "15 * 2 * 2",
        "20 / 2 + 5",
        "7 * 8 - 10",
        "14 / 2 * 3",
        "9 * 3 * 2",
        "100 / 10 + 7",
        "5 * 5 * 5",
        "18 / 3 + 4",
        "11 * 2 - 6",
        "16 / 4 * 5",
        "25 - 5 * 3"
        ]
        )
    
    if belgi == "+":
        answer = a + b
    elif belgi == "-":
        answer = a - b
    elif belgi == "*":
        answer = a * b
    else:
        answer = a / b
    
    tanlaw = [
        [
            InlineKeyboardButton(text="+", callback_data="first"),
            InlineKeyboardButton(text="-", callback_data="second")
        ],
        [
            InlineKeyboardButton(text="*", callback_data="third"),
            InlineKeyboardButton(text="/", callback_data="fourth")
        ]
    ]
    mark = InlineKeyboardMarkup(inline_keyboard=tanlaw)
    await state.update_data(answer=answer, belgi = belgi)
    await message.answer(f"""Iltimas o'zin'iz kerekli dep bilgen belgini saylan'!
{a} ? {b} = {answer}""", reply_markup=mark)