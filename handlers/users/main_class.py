from aiogram import types
from utils import Get_dog
from loader import dp

# декоратор диспечер
@dp.message_handler()
async def get_dog(message: types.Message):
    new_dog = Get_dog()
    await message.answer(new_dog.get_file_json())