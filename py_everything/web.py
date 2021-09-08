import webbrowser

googleUrl: str = "https://google.com/search?q="
ytUrl: str = "https://youtube.com/results?search_query="
githubUrl: str = "https://github.com/search?q="
soUrl: str = "https://stackoverflow.com/search?q="
amz_inUrl: str = "https://www.amazon.in/s?k="
amz_comUrl: str = "https://www.amazon.com/s?k="
pypiUrl: str = "https://pypi.org/search/?q="
rtdocsUrl: str = "https://readthedocs.io/search/?q="


def googleSearch(query: str) -> None:
    """Searches Google"""
    finalUrl: str = googleUrl + query
    webbrowser.open(finalUrl)


def ytSearch(query: str) -> None:
    """Searches YouTube"""
    finalUrl: str = ytUrl + query
    webbrowser.open(finalUrl)


def githubSearch(query: str) -> None:
    """Searches GitHub"""
    finalUrl: str = githubUrl + query
    webbrowser.open(finalUrl)


def soSearch(query: str) -> None:
    """Searches StackOverflow"""
    finalUrl: str = soUrl + query
    webbrowser.open(finalUrl)


def amz_inSearch(query: str) -> None:
    """Searches Amazon.in"""
    finalUrl: str = amz_inUrl + query
    webbrowser.open(finalUrl)


def amz_comSearch(query: str) -> None:
    """Searches Amazon.com"""
    finalUrl: str = amz_comUrl + query
    webbrowser.open(finalUrl)


def pypiSearch(query: str) -> None:
    """Searches PyPI"""
    finalUrl: str = pypiUrl + query
    webbrowser.open(finalUrl)


def rtdocsSearch(query: str) -> None:
    """Searches ReadTheDocs"""
    finalUrl: str = rtdocsUrl + query
    webbrowser.open(finalUrl)


def openNewTab(url: str, query: str):
    """Searches in  New Tab"""
    finalUrl: str = url + query
    webbrowser.open_new_tab(finalUrl)


def openNewWindow(url: str, query: str):
    """Searches in New Window"""
    finalUrl: str = url + query
    webbrowser.open_new(finalUrl)
