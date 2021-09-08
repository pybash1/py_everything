from typing import List, Tuple


def getElementsByTag(tagName: str, fileName: str) -> List[Tuple[int, str]]:
    """Returns all matching tags from an HTML/XML document"""
    nonN: List[str] = []
    with open(fileName, "r+") as f:
        html: List[str] = f.readlines()
        for line in html:
            nonN.append(line.replace("\n", ""))

    pattern: str = f"<{tagName}>"
    patternAlt: str = f"{tagName} />"

    matches: List[Tuple[int, str]] = []

    for line in nonN:
        if pattern in line or patternAlt in line:
            lineNo = nonN.index(line) + 1
            matches.append((int(lineNo), line))
    return matches


def getElementsById(idName: str, fileName: str) -> List[Tuple[int, str]]:
    """Returns all matching tags from an HTML/XML document"""
    nonN: List[str] = []
    with open(fileName, "r+") as f:
        html: List[str] = f.readlines()
        for line in html:
            nonN.append(line.replace("\n", ""))

    pattern: str = f'id="{idName}"'
    patternAlt: str = f"id='{idName}'"

    matches: List[Tuple[int, str]] = []

    for line in nonN:
        if pattern in line or patternAlt in line:
            lineNo = nonN.index(line) + 1
            matches.append((int(lineNo), line))
    return matches


def getElementsByClass(className: str, fileName: str) -> List[Tuple[int, str]]:
    """Returns all matching tags from an HTML/XML document"""
    nonN: List[str] = []
    with open(fileName, "r+") as f:
        html: List[str] = f.readlines()
        for line in html:
            nonN.append(line.replace("\n", ""))

    pattern: str = f'class="{className}"'
    patternAlt: str = f"class='{className}'"

    matches: List[Tuple[int, str]] = []

    for line in nonN:
        if pattern in line or patternAlt in line:
            lineNo = nonN.index(line) + 1
            matches.append((int(lineNo), line))
    return matches


def getElementByTag(tagName: str, fileName: str) -> List[Tuple[int, str]]:
    """Returns first matching tag from an HTML/XML document"""
    nonN: List[str] = []
    with open(fileName, "r+") as f:
        html: List[str] = f.readlines()
        for line in html:
            nonN.append(line.replace("\n", ""))

    pattern: str = f"<{tagName}>"
    patternAlt: str = f"<{tagName} />"

    matches: List[Tuple[int, str]] = []

    for line in nonN:
        if pattern in line or patternAlt in line:
            lineNo = nonN.index(line) + 1
            matches.append((int(lineNo), line))
            break
    return matches


def getElementById(idName: str, fileName: str) -> List[Tuple[int, str]]:
    """Returns first matching tag from an HTML/XML document"""
    nonN: List[str] = []
    with open(fileName, "r+") as f:
        html: List[str] = f.readlines()
        for line in html:
            nonN.append(line.replace("\n", ""))

    pattern: str = f'id="{idName}"'
    patternAlt: str = f"id='{idName}'"

    matches: List[Tuple[int, str]] = []

    for line in nonN:
        if pattern in line or patternAlt in line:
            lineNo = nonN.index(line) + 1
            matches.append((int(lineNo), line))
            break
    return matches


def getElementByClass(className: str, fileName: str) -> List[Tuple[int, str]]:
    """Returns first matching tag from an HTML/XML document"""
    nonN: List[str] = []
    with open(fileName, "r+") as f:
        html: List[str] = f.readlines()
        for line in html:
            nonN.append(line.replace("\n", ""))

    pattern: str = f'class="{className}"'
    patternAlt: str = f"class='{className}'"

    matches: List[Tuple[int, str]] = []

    for line in nonN:
        if pattern in line or patternAlt in line:
            lineNo = nonN.index(line) + 1
            matches.append((int(lineNo), line))
            break
    return matches


class HTMLObject:
    """Class for HTML Object"""

    def __init__(self, fileName: str):
        self.fileName = fileName

    def getElementsByTag(self, tagName: str) -> List[Tuple[int, str]]:
        """Returns all matching tags from an HTML/XML document"""
        nonN: List[str] = []
        with open(self.fileName, "r+") as f:
            html: List[str] = f.readlines()
            for line in html:
                nonN.append(line.replace("\n", ""))

        pattern: str = f"<{tagName}>"

        matches: List[Tuple[int, str]] = []

        for line in nonN:
            if pattern in line:
                lineNo = nonN.index(line) + 1
                matches.append((int(lineNo), line))

        return matches

    def getElementsById(self, idName: str) -> List[Tuple[int, str]]:
        """Returns all matching tags from an HTML/XML document"""
        nonN: List[str] = []
        with open(self.fileName, "r+") as f:
            html: List[str] = f.readlines()
            for line in html:
                nonN.append(line.replace("\n", ""))

        pattern: str = f'id="{idName}"'
        patternAlt: str = f"id='{idName}'"

        matches: List[Tuple[int, str]] = []

        for line in nonN:
            if pattern in line or patternAlt in line:
                lineNo = nonN.index(line) + 1
                matches.append((int(lineNo), line))
        return matches

    def getElementsByClass(self, className: str) -> List[Tuple[int, str]]:
        """Returns all matching tags from an HTML/XML document"""
        nonN: List[str] = []
        with open(self.fileName, "r+") as f:
            html: List[str] = f.readlines()
            for line in html:
                nonN.append(line.replace("\n", ""))

        pattern: str = f'class="{className}"'
        patternAlt: str = f"class='{className}'"

        matches: List[Tuple[int, str]] = []

        for line in nonN:
            if pattern in line or patternAlt in line:
                lineNo = nonN.index(line) + 1
                matches.append((int(lineNo), line))
        return matches

    def getElementByTag(self, tagName: str) -> List[Tuple[int, str]]:
        """Returns all matching tags from an HTML/XML document"""
        nonN: List[str] = []
        with open(self.fileName, "r+") as f:
            html: List[str] = f.readlines()
            for line in html:
                nonN.append(line.replace("\n", ""))

        pattern: str = f"<{tagName}>"
        patternAlt: str = f"<{tagName} />"

        matches: List[Tuple[int, str]] = []

        for line in nonN:
            if pattern in line or patternAlt in line:
                lineNo = nonN.index(line) + 1
                matches.append((int(lineNo), line))
                break
        return matches

    def getElementById(self, idName: str) -> List[Tuple[int, str]]:
        """Returns first matching tag from an HTML/XML document"""
        nonN: List[str] = []
        with open(self.fileName, "r+") as f:
            html: List[str] = f.readlines()
            for line in html:
                nonN.append(line.replace("\n", ""))

        pattern: str = f'id="{idName}"'
        patternAlt: str = f"id='{idName}'"

        matches: List[Tuple[int, str]] = []

        for line in nonN:
            if pattern in line or patternAlt in line:
                lineNo = nonN.index(line) + 1
                matches.append((int(lineNo), line))
                break
        return matches

    def getElementByClass(self, className: str) -> List[Tuple[int, str]]:
        """Returns first matching tag from an HTML/XML document"""
        nonN: List[str] = []
        with open(self.fileName, "r+") as f:
            html: List[str] = f.readlines()
            for line in html:
                nonN.append(line.replace("\n", ""))

        pattern: str = f'class="{className}"'
        patternAlt: str = f"class='{className}'"

        matches: List[Tuple[int, str]] = []

        for line in nonN:
            if pattern in line or patternAlt in line:
                lineNo = nonN.index(line) + 1
                matches.append((int(lineNo), line))
                break
        return matches
