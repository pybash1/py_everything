import random
from typing import List

def randhex() -> str:
    """Returns random hex code as string"""
    return "#" + "".join(random.choices("ABCDEF123456", k=6))

def randRGB() -> tuple:
    """Returns a tuple containing an random RGB value"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return (r, g, b)

def randletter() -> str:
    """Returns arandom alphabet"""
    return random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

def randint(start: int, end: int) -> int:
    """Returns a random integer"""
    return random.randint(start, end)

def randfloat(start: float, end: float) -> float:
    """Returns a random float between `start` and `end`"""
    start = int(start * 10000000)
    end = int(end * 10000000)
    resultList = []
    
    for i in range(start, end):
        resultList.append(i/10000000)
        
    return random.choice(resultList)

def randbool() -> bool:
    """Returns a random boolean"""
    return random.choice([True, False])

def randboolList(len: int) -> List[bool]:
    """Returns a list of booleans generated randomly with length `len`"""
    finalList: List[bool] = []
    
    for i in range(len):
        finalList.append(random.choice([True, False]))
        
    return finalList

def randstring(string: str) -> str:
    """Returns random letter from given `string`"""
    resultList: List[str] = []
    
    for letter in string:
        resultList.append(letter)
        
    return str(random.choice(resultList))

# To round off result returned by randfloat() to 2 decimal places the following can be used
# float(str(randfloat(1.1, 2.3)).split('.')[0]+'.'+str("".join(list(str(randfloat(1.1, 2.3)).split('.')[1])[0:2])))
