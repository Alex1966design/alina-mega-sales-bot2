import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Update
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Tokens and Webhook
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
USE_WEBHOOK = os.getenv("USE_WEBHOOK", "True") == "True"

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

# Handler
@dp.message()
async def handle_message(message: types.Message):
    await message.reply("Hello from Railway bot! 🚀")

# Webhook or polling
async def main():
    if USE_WEBHOOK:
        app = web.Application()
        SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path="/webhook")
        await bot.set_webhook(WEBHOOK_URL)
        setup_application(app, dp, bot=bot)
        return app
    else:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

if USE_WEBHOOK:
    app = asyncio.run(main())
else:
    import asyncio
    asyncio.run(main())
