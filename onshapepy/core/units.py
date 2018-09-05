"""This file defines the OnshapePy units system. This system is dependent on Pint, but this is the only place Pint is mentioned. If any part of OnshapePy uses units, it needs to reference the units used here. Similarly, other applications that use OnshapePy must define units based on the unit registry instantiated here"""

import pint

u = pint.UnitRegistry(system='mks', autoconvert_offset_to_baseunit=True)


