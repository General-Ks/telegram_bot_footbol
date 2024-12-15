import asyncio
from bot.bot import dp, bot  # Импортируем как bot, так и dp
from handlers.handlers import register_handlers

if __name__ == '__main__':
    register_handlers(dp)
    asyncio.run(dp.start_polling(bot))  # Передаем экземпляр бота
