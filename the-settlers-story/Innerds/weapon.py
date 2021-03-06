from BlueDB.blue2 import Blue

"""
TYPES:
    Sword
    Axe
    Bow
    Gun
    CrossBow
    MachineGun

NOTE:
    After looking at the code to "The-Settler (Two different games)" I've noticed that the weapon/armor class and Mod classes are more modifiable with the stats of the weapon being in a dictionary instead of just being attributes of the class. This isnt necessarly good, mainly being because id have to add more code for unknown types and making it hard for players to make mods as they would have to add new Fight mechanics for the new stats they add...
"""

__slot__ = [
    # Const's
    "TYPES",
    "DEFAULT",
    "BASE_MODS",

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
    def registerType(self, name, mod):
        setattr(self, name.upper(), name)
        self._types.append(getattr(self, name.upper()))
        # This should work, if not then shove a FIXME here
        BASE_MODS[name] = mod

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
    name="BaseSword",
    damage=0,
    speed=2,
    depth=4,
    chance=6,
)

BASE_AXE_MOD = Mod(
    name="BaseAxe",
    damage=0,
    speed=4,
    depth=5,
    chance=4
)

BASE_BOW_MOD = Mod(
    name="BaseBow",
    damage=0,
    speed=3,
    depth=7,
    chance=6
)

BASE_GUN_MOD = Mod(
    name="BaseGun",
    damage=2,
    speed=1,
    depth=5,
    chance=1
)

BASE_CROSSBOW_MOD = Mod(
    name="BaseCrossbow",
    damage=1,
    speed=3,
    depth=7,
    chance=4
)

BASE_MACHINEGUN_MOD = Mod(
    name="BaseMachinegun",
    damage=3,
    speed=4,
    depth=1,
    chance=1
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
        self.level = 1
        self.mods = []

        self.damage = 0
        self.speed = 0
        self.depth = 0
        self.chance = 0
        if self.type not in TYPES:
            raise
        else:
            self.mods.append(BASE_MODS[self.type])
        for i in kwargs.get("mods", []):
            self.mods.append(Mod(i))

        for mod in self.mods:
            self.damage += mod.damage
            self.speed += mod.speed
            self.depth += mod.depth
            self.chance += mod.chance

    @property
    def attack(self):
        attack = self.damage
        attack *= self.level
        force = (self.depth*(self.speed/10))+self.depth
        attack = attack+(attack*force)
        return attack
