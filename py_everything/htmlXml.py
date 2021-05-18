def getElementsByTag(tagName: str, fileName: str):
    nonN = []
    with open(fileName, 'r+') as f:
        html = f.readlines()
        for line in html:
            nonN.append(line.replace('\n', ''))
    
    pattern = f"<{tagName}>"
    patternAlt = f"{tagName} />"
    
    matches = []
    
    for line in nonN:
        if pattern in line:
            matches.append(line)
        elif patternAlt in line:
            matches.append(line)
    
    return matches

def getElementsById(idName: str, fileName: str):
    nonN = []
    with open(fileName, 'r+') as f:
        html = f.readlines()
        for line in html:
            nonN.append(line.replace('\n', ''))
    
    pattern = f"id=\"{idName}\""
    patternAlt = f"id='{idName}'"
    
    matches = []
    
    for line in nonN:
        if pattern in line:
            matches.append(line)
        elif patternAlt in line:
            matches.append(line)
    
    return matches

def getElementsByClass(className: str, fileName: str):
    nonN = []
    with open(fileName, 'r+') as f:
        html = f.readlines()
        for line in html:
            nonN.append(line.replace('\n', ''))
    
    pattern = f"class=\"{className}\""
    patternAlt = f"class='{className}'"
    
    matches = []
    
    for line in nonN:
        if pattern in line:
            matches.append(line)
        elif patternAlt in line:
            matches.append(line)
    
    return matches

def getElementByTag(tagName: str, fileName: str):
    nonN = []
    with open(fileName, 'r+') as f:
        html = f.readlines()
        for line in html:
            nonN.append(line.replace('\n', ''))
    
    pattern = f"<{tagName}>"
    patternAlt = f"<{tagName} />"
    
    matches = []
    
    for line in nonN:
        if pattern in line:
            matches.append(line)
            break
        elif patternAlt in line:
            matches.append(line)
            break
    
    return matches

def getElementById(idName: str, fileName: str):
    nonN = []
    with open(fileName, 'r+') as f:
        html = f.readlines()
        for line in html:
            nonN.append(line.replace('\n', ''))
    
    pattern = f"id=\"{idName}\""
    patternAlt = f"id='{idName}'"
    
    matches = []
    
    for line in nonN:
        if pattern in line:
            matches.append(line)
            break
        elif patternAlt in line:
            matches.append(line)
            break
    
    return matches

def getElementByClass(className: str, fileName: str):
    nonN = []
    with open(fileName, 'r+') as f:
        html = f.readlines()
        for line in html:
            nonN.append(line.replace('\n', ''))
    
    pattern = f"class=\"{className}\""
    patternAlt = f"class='{className}'"
    
    matches = []
    
    for line in nonN:
        if pattern in line:
            matches.append(line)
            break
        elif patternAlt in line:
            matches.append(line)
            break
    
    return matches


class HTMLObject:
    def __init__(self, fileName: str):
        self.fileName = fileName
        
    def getElementsByTag(self, tagName: str):
        nonN = []
        with open(self.fileName, 'r+') as f:
            html = f.readlines()
            for line in html:
                nonN.append(line.replace('\n', ''))
        
        pattern = f"<{tagName}>"
        
        matches = []
        
        for line in nonN:
            if pattern in line:
                matches.append(line)
        
        return matches

    def getElementsById(self, idName: str):
        nonN = []
        with open(self.fileName, 'r+') as f:
            html = f.readlines()
            for line in html:
                nonN.append(line.replace('\n', ''))
        
        pattern = f"id=\"{idName}\""
        patternAlt = f"id='{idName}'"
        
        matches = []
        
        for line in nonN:
            if pattern in line:
                matches.append(line)
            elif patternAlt in line:
                matches.append(line)
        
        return matches

    def getElementsByClass(self, className: str):
        nonN = []
        with open(self.fileName, 'r+') as f:
            html = f.readlines()
            for line in html:
                nonN.append(line.replace('\n', ''))
        
        pattern = f"class=\"{className}\""
        patternAlt = f"class='{className}'"
        
        matches = []
        
        for line in nonN:
            if pattern in line:
                matches.append(line)
            elif patternAlt in line:
                matches.append(line)
        
        return matches

    def getElementByTag(self, tagName: str):
        nonN = []
        with open(self.fileName, 'r+') as f:
            html = f.readlines()
            for line in html:
                nonN.append(line.replace('\n', ''))
        
        pattern = f"<{tagName}>"
        patternAlt = f"<{tagName} />"
        
        matches = []
        
        for line in nonN:
            if pattern in line:
                matches.append(line)
                break
            elif patternAlt in line:
                matches.append(line)
                break
        
        return matches

    def getElementById(self, idName: str):
        nonN = []
        with open(self.fileName, 'r+') as f:
            html = f.readlines()
            for line in html:
                nonN.append(line.replace('\n', ''))
        
        pattern = f"id=\"{idName}\""
        patternAlt = f"id='{idName}'"
        
        matches = []
        
        for line in nonN:
            if pattern in line:
                matches.append(line)
                break
            elif patternAlt in line:
                matches.append(line)
                break
        
        return matches

    def getElementByClass(self, className: str):
        nonN = []
        with open(self.fileName, 'r+') as f:
            html = f.readlines()
            for line in html:
                nonN.append(line.replace('\n', ''))
        
        pattern = f"class=\"{className}\""
        patternAlt = f"class='{className}'"
        
        matches = []
        
        for line in nonN:
            if pattern in line:
                matches.append(line)
                break
            elif patternAlt in line:
                matches.append(line)
                break
        
        return matches
