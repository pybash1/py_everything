import datetime

def getDate():
    '''Returns date'''
    date = datetime.date.today()
    return date

def getDateTime():
    '''Returns date and time'''
    dateTime = datetime.datetime.now()
    return dateTime

def getTime():
    '''Returns time'''
    time = datetime.datetime.now().strftime('%H:%M:%S')
    return time

def getCustomFormat(format):
    '''Returns date and/or time in custom format'''
    custom = datetime.datetime.now().strftime(format)
    return custom
