from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

sity= InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Показать список городов' ,callback_data='cities')]
])

backtown= InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вернуться назад' ,callback_data='back_town')]
])

town_view = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пермь' ,callback_data='perm')],
    [InlineKeyboardButton(text='Москва' ,callback_data='moscow')],
    [InlineKeyboardButton(text='Казань' ,callback_data='kazan')],
    [InlineKeyboardButton(text='Тюмень' ,callback_data='tumen')],
    [InlineKeyboardButton(text='Санкт-Петербург' ,callback_data='spb')],
    [InlineKeyboardButton(text='Нижний Новгород' ,callback_data='nn')],
    [InlineKeyboardButton(text='Ижевск' ,callback_data='ez')],
    [InlineKeyboardButton(text='Воронеж' ,callback_data='voronez')],
])

