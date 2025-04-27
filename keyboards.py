from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from system_varibals import FEEDBACK_BTN_TEXT

feedback_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=FEEDBACK_BTN_TEXT)]
    ],resize_keyboard=True
)