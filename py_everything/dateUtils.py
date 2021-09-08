import datetime


def getDate():
    """Returns date"""
    return datetime.date.today()


def getDateTime():
    """Returns date and time"""
    return datetime.datetime.now()


def getTime():
    """Returns time"""
    return datetime.datetime.now().strftime("%H:%M:%S")


def getCustomFormat(format):
    """Returns date and/or time in custom format"""
    return datetime.datetime.now().strftime(format)
