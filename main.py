import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging

# Настройка логгирования
logging.basicConfig(level=logging.INFO)

# Вставь свой токен сюда
BOT_TOKEN = "8175161575:AAFqsXX6Fcx1zhWWB6DxCVOp-8s_EElED64"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Привет! Я бот на aiogram 🚀")

@dp.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer("Доступные команды:\n/start\n/help")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
