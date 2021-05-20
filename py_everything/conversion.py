from typing import Union
from . import units
from . import _data as data

class Mass:
    def __init__(self, unit: Union[units.mg, units.cg, units.dg, units.g, units.dag, units.hg, units.kg], amount: Union[int, float]):
        self.unit = unit
        self.amount = amount

class Volume:
    def __init__(self, unit: Union[units.ml, units.cl, units.dl, units.l, units.dal, units.hl, units.kl], amount: Union[int, float]):
        self.unit = unit
        self.amount = amount

class Length:
    def __init__(self, unit: Union[units.mm, units.cm, units.dm, units.m, units.dam, units.hm, units.km], amount: Union[int, float]):
        self.unit = unit
        self.amount = amount

# Thanks to - http://bit.ly/convertSoHelp - StackOverflow
def convert(fromType: Union[Mass, Volume, Length], toType: Union[Mass, Volume, Length]) -> Union[int, float]:
    amount = fromType.amount
    
    fromTypeUnit = list(fromType.unit.unit)
    toTypeUnit = list(toType.unit.unit)
    
    if len(fromTypeUnit) == 1:
        fromTypeUnit = "base"
    else:
        pass
        
    if len(toTypeUnit) == 1:
        toTypeUnit = "base"
    else:
        pass
    
    fromUnit = data.unitTypes[str(fromTypeUnit[0])]
    toUnit = data.unitTypes[str(toTypeUnit[0])]
    
    postConversion = amount * (fromUnit / toUnit)
    
    return postConversion
