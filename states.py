from aiogram.fsm.state import State, StatesGroup


# Feedback states definition
class FeedbackState(StatesGroup):
    group = State()
    teacher_name = State()
    teacher_p = State()
    teacher_n = State()
    teacher_score = State()
    valiteach = State()
    why_valiteach = State()