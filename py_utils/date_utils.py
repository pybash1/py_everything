import datetime

def get_date():
    date = datetime.date.today()
    return date

def get_date_time():
    dateTime = datetime.datetime.now()
    return dateTime

def get_time():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    return time

def get_custom_format(format):
    custom = datetime.datetime.now().strftime(format)
    return custom

class Date:
    def get_date(self):
        date = datetime.date.today()
        return date

    def get_date_time(self):
        dateTime = datetime.datetime.now()
        return dateTime

    def get_time(self):
        time = datetime.datetime.now().strftime('%H:%M:%S')
        return time

    def get_custom_format(self, format):
        custom = datetime.datetime.now().strftime(format)
        return custom
