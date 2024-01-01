import pandas as pd
from tabulate import tabulate
from datetime import datetime
from habit_tracker import Habit, track_habit

def main():
    habits = [
        track_habit('Gaming', datetime(2024,1,1,8),3, 75),
        track_habit('Youtube', datetime(2024,1,1,8), 3, 60),
        track_habit('Social Media', datetime(2024,1,1,8), 3, 60),
        track_habit('Bubble Gums', datetime(2024,1,1,8), 1, 60),
    ]

    df = pd.DataFrame(habits)

    print(tabulate(df, headers='keys', tablefmt = 'psql'))

if __name__ == '__main__':
    main()