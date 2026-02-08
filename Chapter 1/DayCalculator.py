# Problem: Day Calculator
# Source: https://quera.org/college/3078/chapter/8407/lesson/56077
# Summary: How many days old is the person on a given date using datetime library
# Approach: Using datetime.strptime for input and calculating the days using .days

from datetime import datetime

def day_calculator(date_str):
    birth_date = datetime(1999, 1, 14)
    input_date = datetime.strptime(date_str, "%Y-%m-%d")

    if input_date < birth_date:
        return "Not yet born"

    days_lived = (input_date - birth_date).days
    return days_lived
