import requests

def getR(apiUrl):
    requests.get(apiUrl)

def postR(apiUrl, data):
    requests.post(apiUrl, data=data)

def putR(apiUrl, data):
    requests.put(apiUrl, data=data)

def deleteR(apiUrl):
    requests.delete(apiUrl)

def patchR(apiUrl, data):
    requests.patch(apiUrl, data=data)

def optionsR(apiUrl):
    requests.options(apiUrl)

def headR(apiUrl):
    requests.head(apiUrl)

class ReqLibBase:
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
