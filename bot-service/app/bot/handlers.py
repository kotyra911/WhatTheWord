from aiogram import Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from config import States

import keyboards as kb


router = Router()



@router.message(CommandStart())  # /start command handler
async def start_handler(message: types.Message, bot: Bot, state: FSMContext):

    await bot.send_message(message.chat.id, text="Выбери язык перевода", reply_markup=kb.choose_language())

    await state.set_state(States.wait_for_language)


@router.message(StateFilter(States.wait_for_language), F.text)


