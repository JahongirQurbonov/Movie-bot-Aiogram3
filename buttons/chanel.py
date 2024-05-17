from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import Chanel_id
from aiogram import Bot

KANALLAR = InlineKeyboardMarkup(
    inline_keyboard= [
        [InlineKeyboardButton(text='1-kanal', url='https://t.me/juda_zor_portfolio')],
        [InlineKeyboardButton(text='2-kanal', url='https://t.me/kinobot_p12')]
    ],
    resize_keyboard=True
)

