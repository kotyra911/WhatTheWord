from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


choose_language = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='RU'), KeyboardButton(text='🇺🇸 EN'), KeyboardButton(text='🇪🇸 ES')],
        [KeyboardButton(text='🇫🇷 FR'), KeyboardButton(text='🇩🇪 DE'), KeyboardButton(text='🇨🇳 ZH')],
        [KeyboardButton(text='🇯🇵 JA'), KeyboardButton(text='🇸🇦 AR'), KeyboardButton(text='🇵🇹 PT')],
        [KeyboardButton(text='🇮🇹 IT'), KeyboardButton(text='🇰🇷 KO'), KeyboardButton(text='🇮🇳 HI')],
        [KeyboardButton(text='🇹🇷 TR'), KeyboardButton(text='🇳🇱 NL'), KeyboardButton(text='🇸🇪 SV')],
    ],
    resize_keyboard=True,
)

yes_or_no = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Да'), KeyboardButton(text='Нет')]
    ],
    resize_keyboard=True,
)