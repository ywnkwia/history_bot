import asyncio
import logging

from aiogram import Bot,Dispatcher
from app.handlers.starthandler import router


async def main():
    bot = Bot(token='6998670189:AAEHWJJo7VOpewN943mVf6Hz6MJdjU8EiR8')
    dp = Dispatcher(timeout=40)
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        print('Start work')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot sleep')