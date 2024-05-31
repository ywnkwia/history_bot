from aiogram import F,Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message , CallbackQuery
from aiogram.utils import markdown 

import app.keyboards.inline as kbinline


router = Router()

@router.message(CommandStart())
async def command_start(message:Message):
    text = markdown.text(
        f"~Приветствуем вас в нашем маленьком историческом телеграмм боте.\n\n—Для чего он создан?—\n\n• В первую очередь мы кратко рассказываем историю интересующего вас города, благодаря нашему боту вы сможете узнать о вашем городе чуть больше ,чем просто дату его создания!",
    )
    await message.answer(
        text=text,
        reply_markup=kbinline.sity
    )

@router.callback_query(F.data.startswith('cities'))
async def back_category(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Выберете город, про который хотите узнать:',
                                  reply_markup= kbinline.town_view)
 
@router.callback_query(F.data.startswith(' back'))
async def command_start(message:Message):  
    text = markdown.text(
        f"~Приветствуем вас в нашем маленьком историческом телеграмм боте.\n\n—Для чего он создан?—\n\n• В первую очередь мы кратко рассказываем историю интересующего вас города, благодаря нашему боту вы сможете узнать о вашем городе чуть больше ,чем просто дату его создания!",
    )
    await message.answer(
        text=text,
        reply_markup=kbinline.sity
    )
    
@router.callback_query(F.data.startswith('perm'))
async def view_perm(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo='https://aif-s3.aif.ru/images/015/485/a342d79e148083120d2572cce64ae6b8.jpg',
        caption=f'Название города в разные времена:\nДата создания:\nКраткая история города:'
    )    
@router.callback_query(F.data.startswith('moscow'))
async def view_perm(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo='https://aif-s3.aif.ru/images/015/485/a342d79e148083120d2572cce64ae6b8.jpg',
        caption=f'Название города в разные времена:\nДата создания:\nКраткая история города:'
    )
@router.callback_query(F.data.startswith('kazan'))
async def view_perm(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo='https://aif-s3.aif.ru/images/015/485/a342d79e148083120d2572cce64ae6b8.jpg',
        caption=f'Название города в разные времена:\nДата создания:\nКраткая история города:'
    )
@router.callback_query(F.data.startswith('tumen'))
async def view_perm(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo='https://aif-s3.aif.ru/images/015/485/a342d79e148083120d2572cce64ae6b8.jpg',
        caption=f'Название города в разные времена:\nДата создания:\nКраткая история города:'
    )
@router.callback_query(F.data.startswith('spb'))
async def view_perm(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo='https://aif-s3.aif.ru/images/015/485/a342d79e148083120d2572cce64ae6b8.jpg',
        caption=f'Название города в разные времена:\nДата создания:\nКраткая история города:'
    )
@router.callback_query(F.data.startswith('nn'))
async def view_perm(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo='https://aif-s3.aif.ru/images/015/485/a342d79e148083120d2572cce64ae6b8.jpg',
        caption=f'Название города в разные времена:\nДата создания:\nКраткая история города:'
    )
@router.callback_query(F.data.startswith('ez'))
async def view_perm(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo='https://aif-s3.aif.ru/images/015/485/a342d79e148083120d2572cce64ae6b8.jpg',
        caption=f'Название города в разные времена:\nДата создания:\nКраткая история города:'
    )
@router.callback_query(F.data.startswith('voronez'))
async def view_perm(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer_photo(
        photo='https://aif-s3.aif.ru/images/015/485/a342d79e148083120d2572cce64ae6b8.jpg',
        caption=f'Название города в разные времена:\nДата создания:\nКраткая история города:'
    )
  