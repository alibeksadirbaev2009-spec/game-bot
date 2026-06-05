from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from random import choice
from aiogram.fsm.context import FSMContext
from src.states.auth import AuthStates
from random import randint, choice
from src.keyboards.game import math_symbols
from src.keyboards.restartgame import restart

router = Router()

@router.callback_query(AuthStates.get_answer)
async def check_answer(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    correct = data["belgi"]
    mapping = {
        "first": "+",
        "second": '-',
        "third": "*",
        "fourth": '/'
    }
    user_answer = mapping[callback.data]
    btns = restart()
    if user_answer == correct:
        await callback.message.answer("Duris!", reply_markup=btns)
    else:
        await callback.message.answer(f"Qa'te!\nDuris juwap: {correct}", reply_markup=btns)

    await state.clear()
    await callback.answer()


@router.callback_query(F.data == "re")
async def restart_game(callback: CallbackQuery, state: FSMContext):
        await callback.answer()
        
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

        await state.update_data(belgi=belgi)
        btns = math_symbols()
        await callback.message.answer(f"""Iltimas o'zin'iz kerekli dep bilgen belgini saylan'!
{a} ? {b} = {answer}""",reply_markup=btns)
        await state.set_state(AuthStates.get_answer)
        
        
@router.callback_query(AuthStates.get_answer)
async def check_answer(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    correct = data["belgi"]
    mapping = {
        "first": "+",
        "second": '-',
        "third": "*",
        "fourth": '/'
    }
    user_answer = mapping[callback.data]

    btns = restart()
    if user_answer == correct:
        await callback.message.answer("Duris!", reply_markup=btns)
    else:
        await callback.message.answer(f"Qa'te!\nDuris juwap: {correct}", reply_markup=btns)
    
    await state.clear()
    await callback.answer()

# hands = ['tas', 'qagaz', 'qayshi']

# @router.callback_query(F.data)
# async def callback(call: CallbackQuery):
#     user = call.data
#     bot = choice(hands)
#     if user == bot:
#         await call.message.answer(f"Ten'lik")
#     else:
#         await call.message.answer(f"Ten'lik emes")