import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, Router, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from system_varibals import *
from states import FeedbackState
from keyboards import feedback_keyboard
import importlib
import system_varibals


# Bot token can be obtained via https://t.me/BotFather

bot = Bot(token=TOKEN)

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(text=START_R, reply_markup=feedback_keyboard)


# Temporary data storage


@dp.message(F.text == FEEDBACK_BTN_TEXT)
async def fikr_qoldirish_handler(message: Message, state: FSMContext):
    await state.set_state(FeedbackState.group)
    await message.answer(text=FEEDBACK_BTN_R)

@dp.message(FeedbackState.group)
async def group_handler(message: Message, state: FSMContext):
    malumotlar['group'] = message.text
    await state.set_state(FeedbackState.teacher_name)
    await message.answer(text=GROUP_R)

@dp.message(FeedbackState.teacher_name)
async def teacher_name_handler(message: Message, state: FSMContext):
    malumotlar['teacher_name'] = message.text
    await state.set_state(FeedbackState.teacher_p)
    await message.answer(text=TEACHERNAME_R)

@dp.message(FeedbackState.teacher_p)
async def teacher_p_handler(message: Message, state: FSMContext):
    malumotlar['teacher_p'] = message.text
    await state.set_state(FeedbackState.teacher_n)
    await message.answer(text=TEACHER_P_R)

@dp.message(FeedbackState.teacher_n)
async def teacher_n_handler(message: Message, state: FSMContext):
    malumotlar['teacher_n'] = message.text
    await state.set_state(FeedbackState.teacher_score)
    await message.answer(text=TEACHER_N_R)

@dp.message(FeedbackState.teacher_score)
async def teacher_score_handler(message: Message, state: FSMContext):
    malumotlar['teacher_score'] = message.text
    await state.set_state(FeedbackState.valiteach)
    await message.answer(text=TEACHER_SCORE_R)

@dp.message(FeedbackState.valiteach)
async def valiteach_handler(message: Message, state: FSMContext):
    malumotlar['valiteach'] = message.text
    await state.set_state(FeedbackState.why_valiteach)
    await message.answer(text=LEARNING_CENTER_R)

@dp.message(FeedbackState.why_valiteach)
async def why_valiteach_handler(message: Message, state: FSMContext):
    malumotlar['why_valiteach'] = message.text

    WHY_S_TO = f"""
📢 <b>Yangi Fikr-Mulohaza</b>

📅 <b>📚 Guruh vaqti va kunlari:</b>  
<b>{malumotlar['group']}</b>

👩‍🏫 <b>O‘qituvchi:</b>  
<b>{malumotlar['teacher_name']}</b>

✅ <b>Ijobiy fikrlar:</b>  
{malumotlar['teacher_p']}

⚠️ <b>Tanqidlar:</b>  
{malumotlar['teacher_n']}

🌟 <b>Berilgan baho:</b>  
<b>{malumotlar['teacher_score']}/10</b>

💡 <b>Takliflar:</b>  
{malumotlar['valiteach']}

🎯 <b>Nega {BRAND_NAME}?</b>  
{malumotlar['why_valiteach']}"""

    await state.clear()
    await bot.send_message(chat_id=CHANNEL_ID, text=WHY_S_TO, parse_mode='HTML')
    await message.answer(text=WHY_R)



@dp.message()
async def echo_handler(message: Message) -> None:

    await message.answer(ECHO_R)


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())