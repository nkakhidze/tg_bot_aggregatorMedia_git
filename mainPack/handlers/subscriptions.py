from aiogram import Router, types
import json

router = Router()

# Загрузить подписки
try:
    with open("subscriptions.json", "r", encoding="utf-8") as f:
        subscriptions = json.load(f)
except FileNotFoundError:
    subscriptions = {}

@router.message()
async def save_subscription(message: types.Message):
    user_id = str(message.from_user.id)
    url = message.text.strip()

    if url.startswith("http"):
        subscriptions.setdefault(user_id, []).append(url)
        with open("subscriptions.json", "w", encoding="utf-8") as f:
            json.dump(subscriptions, f, indent=4, ensure_ascii=False)

        await message.answer(f"✅ Я добавил {url} в твою подписку!")
    else:
        await message.answer("❌ Это не похоже на ссылку. Пришли мне URL новости.")
