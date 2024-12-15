import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем API-токен из переменной окружения
API_TOKEN = os.getenv('API_TOKEN')

# Создаем экземпляр бота
bot = Bot(token=API_TOKEN)
# Создаем экземпляр диспетчера
dp = Dispatcher()
