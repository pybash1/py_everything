import webbrowser

googleUrl = 'https://google.com/search?q='
ytUrl = 'https://youtube.com/results?search_query='
githubUrl = 'https://github.com/search?q='
soUrl = 'https://stackoverflow.com/search?q='
amz_inUrl = 'https://www.amazon.in/s?k='
amz_comUrl = 'https://www.amazon.com/s?k='
pypiUrl = 'https://pypi.org/search/?q='
rtdocsUrl = 'https://readthedocs.io/search/?q='

def googleSearch(query):
    finalUrl = googleUrl + query
    webbrowser.open(finalUrl)

def ytSearch(query):
    finalUrl = ytUrl + query
    webbrowser.open(finalUrl)

def githubSearch(query):
    finalUrl = githubUrl + query
    webbrowser.open(finalUrl)

def soSearch(query):
    finalUrl = soUrl + query
    webbrowser.open(finalUrl)

def amz_inSearch(query):
    finalUrl = amz_inUrl + query
    webbrowser.open(finalUrl)

def amz_comSearch(query):
    finalUrl = amz_comUrl + query
    webbrowser.open(finalUrl)

def pypiSearch(query):
    finalUrl = pypiUrl + query
    webbrowser.open(finalUrl)

def rtdocsSearch(query):
    finalUrl = rtdocsUrl + query
    webbrowser.open(finalUrl)

def openNewTab(url, query):
    finalUrl = url + query
    webbrowser.open_new_tab(finalUrl)

def openNewWindow(url, query):
    finalUrl = url + query
    webbrowser.open_new(finalUrl)
