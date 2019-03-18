from BlueDB import Blue

"""
TYPES:
    Sword
    Axe
    Bow
    Gun
    CrossBow
    MachineGun
"""

__slot__ = [
    # Const's
    "TYPES",
    "DEFAULT",
    "BASE_MODS"

    # Classes
    "Mod",
    "Weapon"
]


class _TYPES:
    SWORD = "sword"
    AXE = "axe"
    BOW = "bow"
    GUN = "gun"
    CROSSBOW = "crossbow"
    MACHINEGUN = "machinegun"
    _types = [
        SWORD,
        AXE,
        BOW,
        GUN,
        CROSSBOW,
        MACHINEGUN
    ]

    @classmethod
    def registerType(cls, name, mod):
        setattr(cls, name.upper(), name)
        cls._types.append(getattr(cls, name.upper()))
        BASE_MODS[name] = mod # <- This should work, if not then shove a FIXME here

    def __iter__(self):
        return iter(self._types)


# So __iter__ works for `in` & `not in` expressions
TYPES = _TYPES()

# Dont like having access to the actual __class__ since i dont want any mix ups with __iter__
del _TYPES

DEFAULT = TYPES.SWORD

class Mod:

    def __init__(self, **kwargs):
        """
        name
        damage
        speed
        depth
        chance
        """
        self.name = kwargs.get("name", None)
        self.damage = kwargs.get("damage", 0)
        self.speed = kwargs.get("speed", 0)
        self.depth = kwargs.get("depth", 0)
        self.chance = kwargs.get("chance", 0)

BASE_SWORD_MOD = Mod(
    name = "BaseSword",
    damage = 0,
    speed = 2,
    depth = 4,
    chance = 6,
)

BASE_AXE_MOD = Mod(
    name = "BaseAxe",
    damage = 0,
    speed = 4,
    depth = 5,
    chance = 4
)

BASE_BOW_MOD = Mod(
    name = "BaseBow",
    damage = 0,
    speed = 3,
    depth = 7,
    chance = 6
)

BASE_GUN_MOD = Mod(
    name = "BaseGun",
    damage = 2,
    speed = 1,
    depth = 5,
    chance = 1
)

BASE_CROSSBOW_MOD = Mod(
    name = "BaseCrossbow",
    damage = 1,
    speed = 3,
    depth = 7,
    chance = 4
)

BASE_MACHINEGUN_MOD = Mod(
    name = "BaseMachinegun",
    damage = 3,
    speed = 4,
    depth = 1,
    chance = 1
)

BASE_MODS = {
    TYPES.SWORD: BASE_SWORD_MOD,
    TYPES.AXE: BASE_AXE_MOD,
    TYPES.BOW: BASE_BOW_MOD,
    TYPES.GUN: BASE_GUN_MOD,
    TYPES.CROSSBOW: BASE_CROSSBOW_MOD,
    TYPES.MACHINEGUN: BASE_MACHINEGUN_MOD
}

class Weapon:

    def __init__(self, name, **kwargs):
        self.name = name
        self.type = kwargs.get("type", DEFAULT)
        self.level = 0
        self.mods = []
        if self.type not in TYPES:
            raise
        else:
            self.mods.append(BASE_MODS[self.type]
            )
        for i in kwargs.get("mods", []):
            self.mods.append(Mod(i))

    def addMod(self, mod):
        pass

    @property
    def attack(self):
        attack = self.damage
        attack *= self.level
        force = (self.depth*(self.speed/10))+self.depth
        attack = attack+(attack*force)
        return attack