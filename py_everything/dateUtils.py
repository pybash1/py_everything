import datetime

def getDate():
    date = datetime.date.today()
    return date

def getDateTime():
    dateTime = datetime.datetime.now()
    return dateTime

def getTime():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    return time

def getCustomFormat(format):
    custom = datetime.datetime.now().strftime(format)
    return custom
