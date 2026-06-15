from  aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from src.states.auth import AuthStates, Change_profile
from src.crud.users import UserRepo 

router = Router()

@router.message(AuthStates.name)
async def get_name(message: Message, state: FSMContext):
    name = message.text   

    if not name.isalpha():
        await message.answer(f"Atin'ız tek ha'riplerden ibarat bolsın, eshqanday belgilersiz!")
        return
    
    await state.update_data(name=name)

    await message.answer(f"Atin'izdi qabillandi, endi Familyan'izdi kiritin':")
    await state.set_state(AuthStates.lastname)



@router.message(AuthStates.lastname)
async def state_lastname(message: Message, state: FSMContext):
    lastname = message.text

    if not lastname.isalpha():
        await message.answer(f"Familya'iz tek ha'riplerden ibarat bolsın, eshqanday belgilersiz!")
        return
        
    await state.update_data(lastname=lastname)
    
    await message.answer(f"Familyan'izdi qabillandi, endi jasin'zdi kiritin':")
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
    await state.update_data(age=age)

    await message.answer(f"Jasin'z qabillandi, endi telefon nomerin'izdi kiritin':")
    await state.set_state(AuthStates.phone)



@router.message(AuthStates.phone)
async def state_phone(message: Message, state: FSMContext):
    phone = message.text

    if not phone.isdigit() or len(phone) !=9:
        await message.answer(f"Telefon nomeri sanlarda boliwi ha'm 9 sannan ibarat boliwi kerek!")
        return
        
    await state.update_data(phone=phone)

    await message.answer(f"Telefon nonerin'iz qabillandi, endi manzilin'izdi kritin':")
    await state.set_state(AuthStates.location)



@router.message(AuthStates.location)
async def state_location(message: Message, state: FSMContext):
    await state.update_data(location=message.text)

    data = await state.get_data()

    name = data.get("name")
    lastname = data.get("lastname")
    age = data.get("age")
    phone = data.get("phone")
    location = data.get("location")

    user = await UserRepo.create(
        telegram_id=message.from_user.id,
        first_name=name,
        lastname=lastname,
        age=int(age),
        phone=phone,
        location=location
    )

    if user is not None:
        await message.answer(f"Siz dizimge alindin'iz!")
    else:
        await message.answer(f"Dizimge aliwda qa'telik!")
        
    await state.clear()






@router.message(Change_profile.name)
async def get_name(message: Message, state: FSMContext):
    name = message.text   

    if not name.isalpha():
        await message.answer(f"Atin'ız tek ha'riplerden ibarat bolsın, eshqanday belgilersiz!")
        return
    
    await state.update_data(name=name)

    await message.answer(f"Atin'izdi qabillandi, endi Familyan'izdi kiritin':")
    await state.set_state(Change_profile.lastname)

@router.message(Change_profile.lastname)
async def state_lastname(message: Message, state: FSMContext):
    lastname = message.text

    if not lastname.isalpha():
        await message.answer(f"Familya'iz tek ha'riplerden ibarat bolsın, eshqanday belgilersiz!")
        return
        
    await state.update_data(lastname=lastname)
    
    await message.answer(f"Familyan'izdi qabillandi, endi jasin'zdi kiritin':")
    await state.set_state(Change_profile.age)


@router.message(Change_profile.age)
async def get_age(message: Message, state: FSMContext):
    age = message.text

    if not age.isdigit():
        await message.answer(f"Jas tek sanlarda boladi.")
        return
    
    age = int(age)

    if not 10 <= age <= 80:
        await message.answer(f"Jas shegarasi 10 dan baslanip 80 ge shekem!")
        return
    await state.update_data(age=age)

    await message.answer(f"Jasin'z qabillandi, endi telefon nomerin'izdi kiritin':")
    await state.set_state(Change_profile.phone)

@router.message(Change_profile.phone)
async def state_phone(message: Message, state: FSMContext):
    phone = message.text

    if not phone.isdigit() or len(phone) !=9:
        await message.answer(f"Telefon nomeri sanlarda boliwi ha'm 9 sannan ibarat boliwi kerek!")
        return
        
    await state.update_data(phone=phone)

    await message.answer(f"Telefon nonerin'iz qabillandi, endi manzilin'izdi kritin':")
    await state.set_state(Change_profile.location)

@router.message(Change_profile.location)
async def state_location(message: Message, state: FSMContext):
    await state.update_data(location=message.text)

    data = await state.get_data()

    name = data.get("name")
    lastname = data.get("lastname")
    age = data.get("age")
    phone = data.get("phone")
    location = data.get("location")

    await UserRepo.update_profile(
        telegram_id=message.from_user.id,
        data={
            "first_name": name,
            "lastname": lastname,
            "age": age,
            "phone": phone,
            "location": location
        }
    )
    await state.clear()

    await message.answer(f"Profile jan'alandi")
    
# BOUND - I/O -sirttag'i - async,        CPU - sync
