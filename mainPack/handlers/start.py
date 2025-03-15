from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Привет! Я новостной бот. Пришли мне ссылку на новостной сайт, и я буду отправлять тебе обновления.")