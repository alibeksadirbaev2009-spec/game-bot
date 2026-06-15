from  aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from src.states.auth import AuthStates

router = Router()


@router.message(F.text == "register")
async def start_register(message: Message, state: FSMContext):
    await message.answer("Atin'izdi kiritin':")
    await state.set_state(AuthStates.name)