import asyncio
from aiogram import Bot, Dispatcher, types
from config import TOKEN
from app.bot.handlers import router


async def main():

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    # Clear message queue
    await bot.get_updates(offset=-1)

    await dp.start_polling(bot)
    print('старт')

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\n!BOT STOP!\n')
