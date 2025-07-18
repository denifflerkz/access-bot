from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import logging
from datetime import datetime

API_TOKEN = '8145775053:AAGPlSdGrLRNbmxvLBRqZGU8BnwlNyTX7SA'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

group_link = "https://t.me/+JLZTHLGNzn4wYjcy"

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("✅ Принять условия"))
    await message.answer(
        "👋 Привет! Это тестовый бот.\n\n"
        "Чтобы получить доступ в группу, нажмите кнопку ниже.",
        reply_markup=kb
    )

@dp.message_handler(lambda message: message.text == "✅ Принять условия")
async def handle_accept(message: types.Message):
    user_id = message.from_user.id
    log_entry = f"{datetime.now().isoformat()} - User ID: {user_id}\n"
    with open("accepted_users.log", "a") as f:
        f.write(log_entry)
    await message.answer(
        f"🎉 Спасибо! Вот ссылка на группу:\n👉 {group_link}"
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
