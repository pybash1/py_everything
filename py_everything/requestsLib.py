import requests

def getR(apiUrl):
    response = requests.get(apiUrl)
    return response

def postR(apiUrl, data=None):
    response = requests.post(apiUrl, data)
    return response

def putR(apiUrl, data=None):
    response = requests.put(apiUrl, data)
    return response

def deleteR(apiUrl):
    response = requests.delete(apiUrl)
    return response

def patchR(apiUrl, data=None):
    response = requests.patch(apiUrl, data)
    return response

def optionsR(apiUrl):
    response = requests.options(apiUrl)
    return response

def headR(apiUrl):
    response = requests.head(apiUrl)
    return response

def getContent(response):
    return response.content

def getText(response):
    return response.text

def getJson(response):
    return response.json

def getHeader(response):
    return response.headers

def getSpecificHeader(response, headerName):
    return response.headers[headerName]

class ReqLibBase:
    def __init__(self, apiUrl):
        self.apiUrl = apiUrl
        self.response = ''

    def getR(self, apiUrl):
        self.response = requests.get(apiUrl)

    def postR(self, apiUrl, data):
        self.response = requests.post(apiUrl, data=data)

    def getContent(self, response):
        return response.content

    def getText(self, response):
        return response.text

class ReqLibAdvanced:
    def __init__(self, apiUrl):
        self.apiUrl = apiUrl
        self.response = ''

    def getR(self, apiUrl):
        self.response = requests.get(apiUrl)

    def postR(self, apiUrl, data):
        self.response = requests.post(apiUrl, data=data)

    def putR(self, apiUrl, data):
        self.response = requests.put(apiUrl, data=data)

    def deleteR(self, apiUrl):
        self.response = requests.delete(apiUrl)

    def patchR(self, apiUrl, data):
        self.response = requests.patch(apiUrl, data=data)

    def optionsR(self, apiUrl):
        self.response = requests.options(apiUrl)

    def headR(self, apiUrl):
        self.response = requests.head(apiUrl)

    def getContent(self, response):
        return response.content

    def getText(self, response):
        return response.text

    def getJson(self, response):
        return response.json

    def getHeader(self, response):
        return response.headers

    def getSpecificHeader(self, response, headerName):
        return response.headers[headerName]
