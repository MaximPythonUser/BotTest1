import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

API_BOT = "BOT_TOKEN"

bot = Bot(API_BOT)
dp = Dispatcher()
async def main():
    print("Bot started")
    await dp.start_polling(bot)


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет, я твой первый бот!")

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Чем могу помочь?")

if __name__ == '__main__':
    asyncio.run(main())
