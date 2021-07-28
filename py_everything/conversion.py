from typing import Union, List
from . import units
from . import _data as data

class Mass:
    """Class for mass units"""
    def __init__(self, unit: Union[units.mg, units.cg, units.dg, units.g, units.dag, units.hg, units.kg], amount: Union[int, float]):
        self.unit = unit
        self.amount = amount

class Volume:
    """Class for volume units"""
    def __init__(self, unit: Union[units.ml, units.cl, units.dl, units.l, units.dal, units.hl, units.kl], amount: Union[int, float]):
        self.unit = unit
        self.amount = amount

class Length:
    """Class for length units"""
    def __init__(self, unit: Union[units.mm, units.cm, units.dm, units.m, units.dam, units.hm, units.km], amount: Union[int, float]):
        self.unit = unit
        self.amount = amount

# Thanks to - http://bit.ly/convertSoHelp - StackOverflow
def convert(fromType: Union[Mass, Volume, Length], toType: Union[Mass, Volume, Length]) -> Union[int, float]:
    """Converts from one unit to another"""
    amount: Union[int, float] = fromType.amount
    
    fromTypeUnit: List[str] = list(fromType.unit.unit)
    toTypeUnit: List[str] = list(toType.unit.unit)
    
    if len(fromTypeUnit) == 1:
        fromTypeUnit[0] = "b"
    else:
        pass
        
    if len(toTypeUnit) == 1:
        toTypeUnit[0] = "b"
    else:
        pass
    
    fromUnit: Union[int, float] = data.unitTypes[str(fromTypeUnit[0])]
    toUnit: Union[int, float] = data.unitTypes[str(toTypeUnit[0])]
    
    postConversion: Union[int, float] = amount * (fromUnit / toUnit)
    
    return postConversion
