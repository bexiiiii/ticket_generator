import random
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, FSInputFile
from PIL import Image, ImageDraw, ImageFont

TOKEN = "7607320844:AAH-tge1uk40dyOUw2yBZcDbUBs7IerZev0"
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def generate_image(message: Message):
    text = message.text.split(",")  # Ожидается ввод: "Имя, Номер стола"
    
    if len(text) < 2:
        await message.reply("Введите данные в формате: Имя, Номер стола")
        return
    
    name, table_number = text[0].strip(), text[1].strip()
    random_number = random.randint(1000, 9999)

    # Открываем шаблон
    img = Image.open("template.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("KZ_SamsungSharpSans.ttf", 70)  # Убедись, что шрифт есть в папке

    # Позиции текста на изображении
    draw.text((2000, 180), f"{name}", font=font, fill="white")
    draw.text((1865, 408), f"{table_number}", font=font, fill="white")
    draw.text((2000, 655), f"{random_number}", font=font, fill="white")

    # Сохранение изображения
    img.save("output.png")

    # Используем FSInputFile для отправки
    photo = FSInputFile("output.png")
    await message.answer_photo(photo=photo)

    # Удаляем файл после отправки
    os.remove("output.png")

    # Отправка нового сообщения с просьбой ввести данные
    await message.answer("Отправьте данные  следуещого в формате: Имя, Номер стола")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
