import asyncio
import logging
import sys
from os import getenv
import os
from aiogram.types import Message
from aiogram import Bot, Dispatcher, html, F, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from da_base.sql import read_db
from config import TOKEN, Chanel_id
from states.statets import next_step
from aiogram.fsm.context import FSMContext
from buttons.reply import KINO
from buttons.chanel import KANALLAR
from da_base.sql import add_movie



bot = Bot(token=TOKEN)
dp = Dispatcher()

async def check_subscription(user_id):
    member = await bot.get_chat_member(chat_id=Chanel_id, user_id=user_id)
    return member.status in ['member', 'administrator', 'creator']

@dp.message(CommandStart())
async def start_handler(message: Message):
    user_id = message.from_user.id 
    if await check_subscription(message.from_user.id):
        await message.reply(f"Salom! Botdan foydalanishingiz mumkin:\nKino kodini kiriting!")
    else:
        await message.reply("Botdan foydalanish uchun kanalga obuna bo'lishingiz kerak.", reply_markup=KANALLAR)

@dp.callback_query(lambda callback_query: True)
async def handle_callback_query(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    if await check_subscription(user_id):
        await bot.send_message(user_id, "Rahmat! Siz kanalga obuna bo'lgansiz.")
    else:
        await bot.answer_callback_query(callback_query.id, text="Kanalga obuna bo'lishingiz kerak!", show_alert=True)






# admin 
@dp.message(Command('admin'), F.from_user.id==869782087)
async def admin_cmd(message: Message):
    await message.answer('Glad to see you, Boss😎', reply_markup=KINO)

@dp.message(F.text=='Kino qo\'shish')
async def name(message:Message,state:FSMContext):
    await message.answer('Kino kodini kiriting')
    await state.set_state(next_step.kino_id)

@dp.message(F.text,next_step.kino_id)
async def name(message:Message,state:FSMContext):
    kod = int(message.text)
    
    await state.update_data({
        'kod':kod
    })
    await message.answer('Kino nomini kiriting')
    await state.set_state(next_step.name)

@dp.message(F.text,next_step.name)
async def name(message:Message,state:FSMContext):
    name = message.text
    await state.update_data({
        'name':name
    })
    await message.answer('Kino haqida: ')
    await state.set_state(next_step.des)
    
@dp.message(F.text,next_step.des)
async def name(message:Message,state:FSMContext):
    des = message.text
    await state.update_data({
        'des':des
    })
    await message.answer('kino urlini kiriting')
    await state.set_state(next_step.url)

@dp.message(F.text,next_step.url)
async def name(message:Message,state:FSMContext):
    data = await state.get_data()
    id = data.get('kod')
    name = data.get('name')
    des = data.get('des')
    url = message.text
    add_movie(id,name,des,url)
    await message.answer('db_base saved🤗')
    await state.clear()


#Users
@dp.message(F.text)
async def kodkino(message:Message):
    kod = message.text
    if kod.isdigit():
        for i in read_db():
            if i[0] == int(kod):
                await message.answer_video(video=f"{i[3]}!", caption=f"Kino kodi: #{i[0]}\n{i[1]}\n\n{i[2]}")
                break
        else:
            await message.answer("Bu kodda kino mavjud emas😌")
    else:
        await message.answer("Kechirasiz hozircha text qabul qila olmaymiz🙄")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())