from aiogram import F, Router
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from random import choice
from aiogram.fsm.context import FSMContext
from src.states.auth import AuthStates
import random

router = Router()

# hands = ['tas', 'qagaz', 'qayshi']

# @router.callback_query(F.data)
# async def callback(call: CallbackQuery):
#     user = call.data
#     bot = choice(hands)
#     if user == bot:
#         await call.message.answer(f"Ten'lik")
#     else:
#         await call.message.answer(f"Ten'lik emes")


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

    if user_answer == correct:
        restart = [
            [
                InlineKeyboardButton(text="Qaytadan oynaw", callback_data="re")
            ]
        ]
        mark = InlineKeyboardMarkup(inline_keyboard=restart)
        await callback.message.answer("Duris!", reply_markup=mark)
    else:
        reestart = [
            [
                InlineKeyboardButton(text="Qaytadan oynaw", callback_data="re")
            ]
        ]
        k = InlineKeyboardMarkup(inline_keyboard=reestart)
        await callback.message.answer(f"Qa'te!\nDuris juwap: {correct}", reply_markup=k)


    await state.clear()
    await callback.answer()



@router.callback_query(F.data == "re")
async def restart_game(callback: CallbackQuery, state: FSMContext):
        await callback.answer()
        

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

        await state.update_data(answer=answer, belgi=belgi)
        await state.set_state(AuthStates.get_answer)

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
        await callback.message.answer(f"""Iltimas o'zin'iz kerekli dep bilgen belgini saylan'!
{a} ? {b} = {answer}""",reply_markup=mark)
        
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

    if user_answer == correct:
        restart = [
            [
                InlineKeyboardButton(text="Qaytadan oynaw", callback_data="re")
            ]
        ]
        mark = InlineKeyboardMarkup(inline_keyboard=restart)
        await callback.message.answer("Duris!", reply_markup=mark)
    else:
        reestart = [
            [
                InlineKeyboardButton(text="Qaytadan oynaw", callback_data="re")
            ]
        ]
        k = InlineKeyboardMarkup(inline_keyboard=reestart)
        await callback.message.answer(f"Qa'te!\nDuris juwap: {correct}", reply_markup=k)


    await state.clear()
    await callback.answer()