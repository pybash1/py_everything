********************************
:mod:`py_everything.conversion`
********************************

.. module:: py_everything.conversion

**Source code:** `py_everything/conversion.py <https://github.com/pybash1/py_everything/blob/master/py_everything/conversion.py>`_

This module conatins classes for conversion like, Mass, Length, etc.
And it deals with conversion of units.

.. class:: Mass(unit, amount)

    This class is used for creating an object for Mass values and units

    .. code:: python

        >>> from py_everything.conversion import Mass, convert
        >>> from py_everything.units import mg, g
        >>> mymass = Mass(units.mg(), 1000)
        >>> mymass2 = Mass(units.g(), 1000)
        >>> converted = convert(mymass, mymass2)
        >>> converted
        1.0

    :param Union unit: Any mass unit class from ``units`` module.
    :param int amount: Value of unit.

    .. note::

        Even though amount is given input to both Mass classes, the amount in fromType is only used.

.. class:: Volume(unit, amount)

    This class is used for creating an object for Volume values and units

    .. code:: python

        >>> from py_everything.conversion import Volume, convert
        >>> from py_everything.units import l, ml
        >>> mymass = Mass(units.l(), 1)
        >>> mymass2 = Mass(units.ml(), 1)
        >>> converted = convert(mymass, mymass2)
        >>> converted
        1000.0

    :param Union unit: Any volume unit class from ``units`` module.
    :param int amount: Value of unit.

    .. note::

        Even though amount is given input to both Volume classes, the amount in fromType is only used.

.. class:: Length(unit, amount)

    This class is used for creating an object for Length values and units

    .. code:: python

        >>> from py_everything.conversion import Length, convert
        >>> from py_everything.units import mm, m
        >>> mymass = Mass(units.mm(), 500)
        >>> mymass2 = Mass(units.m(), 1000)
        >>> converted = convert(mymass, mymass2)
        >>> converted
        0.5

    :param Union unit: Any length unit class from ``units`` module.
    :param int amount: Value of unit.

    .. note::

        Even though amount is given input to both Length classes, the amount in fromType is only used.

.. function:: convert(fromType, toType)

    Converts value from unit to another.

    :param Union fromType: Unit to convert from.
    :param Union toType: Unit to convert to.
    :returns float: Value after conversion.
