import datetime

def getDate():
    date = datetime.date.today()
    print(date)

def getDateTime():
    dateTime = datetime.datetime.now()
    print(dateTime)

def getTime():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    print(time)

def getCustomFormat(format):
    custom = datetime.datetime.now().strftime(format)
    print(custom)

class Date:
    def getDate(self):
        date = datetime.date.today()
        print(date)

    def getDateTime(self):
        dateTime = datetime.datetime.now()
        print(dateTime)

    def getTime(self):
        time = datetime.datetime.now().strftime('%H:%M:%S')
        print(time)

    def getCustomFormat(self, format):
        custom = datetime.datetime.now().strftime(format)
        print(custom)
