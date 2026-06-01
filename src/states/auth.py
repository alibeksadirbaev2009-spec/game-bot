from aiogram.fsm.state import StatesGroup, State

class AuthStates(StatesGroup):
    name = State()
    lastname = State()
    age = State()
    phone = State()
    location = State()