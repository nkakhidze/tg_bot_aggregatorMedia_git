from aiogram import Router, types
from services.parser import fetch_news

router = Router()

@router.message()
async def get_news(message: types.Message):
    """Принимает ссылку и парсит новость"""
    print(f"Получено сообщение: {message.text}")
    url = message.text.strip()
    if url.startswith("http"):
        news = fetch_news(url)
        await message.answer(news)
    else:
        await message.answer("❌ Пришли мне ссылку на новость.")
