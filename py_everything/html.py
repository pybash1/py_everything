def getElementsByTag(tagName, fileName):
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
        elif patternAlt in line:
            matches.append(line)
    
    return matches

def getElementsById(idName, fileName):
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

def getElementsByClass(className, fileName):
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

def getElementByTag(tagName, fileName):
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

def getElementById(idName, fileName):
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

def getElementByClass(className, fileName):
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
    def __init__(self, fileName):
        self.fileName = fileName
        
    def getElementsByTag(self, tagName):
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
            elif patternAlt in line:
                matches.append(line)
        
        return matches

    def getElementsById(self, idName):
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

    def getElementsByClass(self, className):
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

    def getElementByTag(self, tagName):
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

    def getElementById(self, idName):
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

    def getElementByClass(self, className):
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

# result = getElementsByTag("div", "index.html")
# print(result)
# result = getElementsById("app", "index.html")
# print(result)
# result = getElementsByClass("app", "index.html")
# print(result)
# result = getElementByTag("p", "index.html")
# print(result)
# result = getElementById("app", "index.html")
# print(result)
# result = getElementByClass("app", "index.html")
# print(result)
