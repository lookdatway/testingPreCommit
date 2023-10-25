import datetime


def get_age(yyyy: int, mm: int, dd: int) -> int:
    dob = datetime.date(yyyy, mm, dd)
    today = datetime.date.today()
    age = (today - dob).days / 365.25
    return age


def sum(yyyy: int, mm: int, dd: int) -> int:

    return yyyy + mm + dd
