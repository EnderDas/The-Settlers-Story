from BlueDB import Blue

"""
TYPES:
    Basic
    Hardened
    Plated
    Thick
    Special
    Mechasuit
"""

__slot__ = [
    # Const's
    "TYPES",
    "DEFAULT",
    "BASE_MODS",

    # Classes
    "Mod",
    "Armor"
]

class _TYPES:
    BASIC = "basic"
    HARDENED = "hardened"
    PLATED = "plated"
    THICK = "thick"
    SPECIAL = "special"
    MECHASUIT = "mechasuit"
    _types = [
        BASIC,
        HARDENED,
        PLATED,
        THICK,
        SPECIAL,
        MECHASUIT
    ]

    def __iter__(self):
        return iter(self._types)

    def registerType(self, name, mod):
        setattr(self, name.upper(), name)
        self._types.append(getattr(self, name.upper()))
        # This should work, if not then shove a FIXME here
        BASE_MODS[name] = mod

# I have the same feelings about this as the one in weapon.py because its the same exact thing as in weapon.py
TYPES = _TYPES()
del _TYPES
DEFAULT = TYPES.BASIC

class Mod:

    def __init__(self, **kwargs):
        """
        name
        sheild
        rebound
        sink
        chance
        """
        self.name = kwargs.get("name", None)
        self.shield = kwargs.get("shield", 0)
        self.rebound = kwargs.get("rebound", 0)
        self.sink = kwargs.get("sink", 0)
        self.chance = kwargs.get("chance", 0)

BASE_BASIC_MOD = Mod(
    name = "BaseBasic",
    shield = 0,
    rebound = 0,
    sink = 0,
    chance = 0,
)
BASE_HARDENED_MOD = Mod(
    name = "BaseHardened"
)
BASE_PLATED_MOD = Mod(
    name = "BasePlated"
)
BASE_THICK_MOD = Mod(
    name = "BaseThick"
)
BASE_SPECIAL_MOD = Mod(
    name = "BaseSpecial"
)
BASE_MECHASUIT_MOD = Mod(
    name = "BaseMechasuit"
)

BASE_MODS = {
    TYPES.BASIC: BASE_BASIC_MOD,
    TYPES.HARDENED: BASE_HARDENED_MOD,
    TYPES.PLATED: BASE_PLATED_MOD,
    TYPES.THICK: BASE_THICK_MOD,
    TYPES.SPECIAL: BASE_SPECIAL_MOD,
    TYPES.MECHASUIT: BASE_MECHASUIT_MOD
}

class Armor:

    def __init__(self, name, **kwargs):
        self.name = name
        self.type = kwargs.get("type", DEFAULT)
        self.level = 1
        self.mods = []

        self.shield = 0
        self.rebound = 0
        self.sink = 0
        self.chance = 0
        if self.type not in TYPES:
            raise
        else:
            self.mods.append(BASE_MODS[self.type])
        for i in kwargs.get("mods", []):
            self.mods.append(Mod(i))
        
        for mod in self.mods:
            self.shield += mod.shield
            self.rebound += mod.rebound
            self.sink += mod.sink
            self.chance += mod.chance

    @property
    def defense(self):
        defense = self.shield
        defense *= self.level
        force = (self.sink*(self.rebound/10))+self.sink
        defense = defense+(defense*force)
        return defense
        