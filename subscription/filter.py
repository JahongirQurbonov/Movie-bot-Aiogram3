
from aiogram import Bot
from aiogram.types import Message
from aiogram.filters import Filter
from config import Chanel_id
from buttons.chanel import KANALLAR

# class  CheksupChanel(Filter):
#     async def __call__(self, message: Message, bot: Bot):
#         for i in Chanel_id:
#             user_status = await bot.get_chat_member(i, message.from_user.id)
#             if user_status.status in ['creator', 'administrator', "member"]:
#                 return True
#             else:
#                 await bot.send_message(chat_id=message.from_user.id,text='❌ Kechirasiz botimizdan foydalanishdan oldin ushbu kanallarga a\'zo bo\'lishingiz kerak.',reply_markup=KANALLAR.as_markup())
#                 return False

async def check_subscription(user_id, bot: Bot):
    member = await bot.get_chat_member(chat_id=Chanel_id, user_id=user_id)
    return member.status in ['member', 'administrator', 'creator']
