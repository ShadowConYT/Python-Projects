from dataclasses import dataclass
from datetime import datetime

@dataclass
class Habit:
    name: str
    time_since: str
    remaining_days: str
    money_saved: str
    minutes_saved: float

def track_habit(name, starttime, cost, minutes_used):
    goal = 60
    wage = 30

    time_elapsed = (datetime.now() - starttime).total_seconds()
    hours = round(time_elapsed / 60 / 60, 1)
    days = round(hours/24,1)

    money_saved = (days * cost)
    minutes_used = round(days * minutes_used)
    total_money_saved = f"({round(money_saved + (minutes_used / 60 * wage),2) })"

    days_to_go = round(goal - days)

    remaining_days = "Cleared" if days_to_go <= 0 else f'{days_to_go}'
    time_since = f'{days} days' if days_to_go > 72 else f'{hours} hours'

    return Habit(name=name, 
                time_since=time_since, 
                remaining_days=remaining_days, 
                minutes_saved=minutes_used,
                money_saved=money_saved)