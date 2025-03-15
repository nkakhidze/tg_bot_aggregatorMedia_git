from aiogram import Router

router = Router()

@router.message()
async def handle_subscriptions(message):
    await message.answer("Функция подписок в разработке.")