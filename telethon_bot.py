from telethon import TelegramClient, events
import asyncio
import os

# Замените на свои данные или используйте .env
API_ID = int(os.getenv("API_ID", "вставь_сюда_свой_api_id"))
API_HASH = os.getenv("API_HASH", "вставь_сюда_свой_api_hash")
PHONE = os.getenv("PHONE", "+7...")  # номер в международном формате

client = TelegramClient("anon", API_ID, API_HASH)

@client.on(events.NewMessage)
async def handler(event):
    if 'привет' in event.raw_text.lower():
        await event.reply("Привет от Telethon бота!")

async def main():
    await client.start(phone=PHONE)
    print("✅ Бот Telethon запущен.")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
