from aiogram.fsm.state import State, StatesGroup

class next_step(StatesGroup):
    kino_id = State()
    name = State()
    des = State()
    url = State()

class start_step(StatesGroup):
    start_bot = State()

    
