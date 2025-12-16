from aiogram import Router
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from config import States, languages, funny_photo
from aiogram import F
from app.bot import keyboards as kb
from app.redis.interaction import RedisInteraction as RI


router = Router()

short_storage = {}



@router.message(CommandStart())  # /start command handler
async def start_handler(message: types.Message, bot: Bot, state: FSMContext):
    print('поймал старт')

    await bot.send_message(message.from_user.id, text="Выбери язык перевода", reply_markup=kb.choose_language)

    await state.set_state(States.wait_for_language)




@router.message(StateFilter(States.wait_for_language), F.text.in_(languages))
async def catch_language(message: types.Message, bot: Bot, state: FSMContext):

    print('поймал язык')
    add_result = await RI.add_user_language(message.from_user.id, message.text)

    if add_result:

        await bot.send_message(message.from_user.id, text="Теперь можешь писать мне любое слово!\n"
                                                      "Можно даже небольшое предложение")

        await state.set_state(States.wait_for_words)

    else:
        await bot.send_message(message.from_user.id,
                               text="У тебя уже выбран язык.\n"
                                   f"Хочешь сменить на {message.text}?",
                               reply_markup=kb.yes_or_no)

        short_storage[message.from_user.id] = message.text

        await state.set_state(States.are_you_sure)


@router.message(StateFilter(States.are_you_sure), F.text.in_(['Да', 'Нет']))
async def catch_are_you_sure(message: types.Message, bot: Bot, state: FSMContext):

    if message.text == 'Да':

        await RI.add_user_language(message.from_user.id, short_storage.get(message.from_user.id))

        del short_storage[message.from_user.id]

        await bot.send_message(message.from_user.id,text='Готово!')

    else:
        await bot.send_photo(message.from_user.id, photo=funny_photo, caption="Спасибо, что просто так потыкал на кнопки!")



