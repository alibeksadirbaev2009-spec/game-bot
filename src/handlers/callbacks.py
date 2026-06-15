from aiogram import F, Router
from aiogram.types import CallbackQuery
from random import choice
from src.crud.users import UserRepo

router = Router()


hands = ['rock', 'paper', 'scissor']


@router.callback_query(F.data)
async def play_game(call: CallbackQuery):
    await call.message.delete()
    await call.answer()

    user = call.data
    bot = choice(hands)


    if user == bot:
        result = "Ten'lik"
        await UserRepo.update_points(
            telegram_id = call.from_user.id,
            tie = 1
        )

    elif (
        (user == 'rock' and bot == 'scissor') or
        (user == 'paper' and bot == 'rock') or
        (user == 'scissor' and bot == 'paper')
    ):
        result = "Siz uttin'iz"
        await UserRepo.update_points(
            telegram_id = call.from_user.id,
            point = 1
        )

    elif (
        (user == 'rock' and bot == 'paper') or 
        (user == 'paper' and bot == 'scissor') or
        (user == 'scissor' and bot == 'rock')
    ):
        result = "Bot utti"
        await UserRepo.update_points(
            telegram_id = call.from_user.id,
            defeat = 1
        )

    else:
        result = "Qa'telik"
        

    await call.message.answer(f"Siz: {user}\nBot: {bot}\nNa'tiyje: {result}")

# @router.callback_query(F.data == "re")
# async def restart_game(call: CallbackQuery):
#     await call.answer()

#     user = call.data
#     bot = choice(hands)


#     if user == bot:
#         result = "Ten'lik"

#     elif (
#         (user == 'stone' and bot == 'scissor') or
#         (user == 'paper' and bot == 'stone') or
#         (user == 'scissor' and bot == 'paper')
#     ):
#         result = "Siz uttin'iz"

#     else:
#         result = "Bot utti"

#     await call.message.answer(f"Siz: {user}\nBot: {bot}\nNa'tiyje: {result}", reply_markup=restart())
#     await call.message.answer("Taza oyin baslaw!",
#     reply_markup=game())