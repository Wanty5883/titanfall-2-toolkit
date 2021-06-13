import tracemalloc
import pandas as pd
import dask.dataframe as dd
import time

def tracing_start():
    tracemalloc.stop()
    print("nTracing Status : ", tracemalloc.is_tracing())
    tracemalloc.start()
    print("Tracing Status : ", tracemalloc.is_tracing())


def tracing_mem():
    first_size, first_peak = tracemalloc.get_traced_memory()
    peak = first_peak/(1024*1024)
    print("Peak Size in MB - ", peak)

class FRONTEND(object):
    ALTERNATOR = {
        "desc": "Twin Barrel SMG.",
        "longdesc": "The Alternator (also referred to as the SP-14 Hatchet in concept art) is a Pilot anti-personnel twin-barrel submachine gun manufactured by Emslie Tactical.",
        "name": "Alternator",
        "nameshort": "alternator",
        "class": "pilot_primary",
        "type": "smg",
    }

    ARCHER = {
        "desc": "Rocket Launcher with Anti-Titan lock-on.",
        "longdesc": "The Archer Heavy Rocket, also known simply as the Archer, is an anti-Titan lock-on rocket launcher manufactured by Brockhaurd Manufacturing.",
        "name": "Archer",
        "nameshort": "archer",
        "class": "pilot_at",
        "type": "anti_titan",
    }

    CAR = {
        "desc": "Consistent recoil SMG.",
        "longdesc": "The Combat Advanced Round Submachine Gun (C.A.R. SMG) is a Pilot anti-personnel fully automatic submachine gun that appears in Titanfall and Titanfall 2",
        "name": "CAR",
        "nameshort": "car",
        "class": "pilot_primary",
        "type": "smg",
    }

    COLDWAR = {
        "desc": "4-round burst Grenadier weapon.",
        "longdesc": "The EM-4 Cold War is a primary four-round burst bullpup grenade launcher manufactured by Vinson Dynamics, firing 4.73x33mm explosive ammunition.",
        "name": "EM-4 Cold War",
        "nameshort": "coldwar",
        "class": "pilot_primary",
        "type": "grenadier",
    }

    DEFENDER = {
        "desc": "Charged precision beam Anti-Titan sniper.",
        "longdesc": "The Charge Rifle fires an energy beam that inflicts massive damage. Holding the trigger charges the weapon.",
        "name": "Charge Rifle",
        "nameshort": "defender",
        "class": "pilot_at",
        "type": "anti_titan",
    }

    DEVOTION = {
        "desc": "Ramps up fire rate over time.",
        "longdesc": "The X-55 Devotion is a light machine guns (LMGs). Its fire rate increases greatly the longer the trigger is held.",
        "name": "X-55 Devotion",
        "nameshort": "devotion",
        "class": "pilot_primary",
        "type": "lmg",
    }

    DOUBLETAKE = {
        "desc": "Twin-fire sniper rifle.",
        "longdesc": "The D-2 Double Take is a Pilot anti-personnel semi-automatic twin-barrel bullpup marksman rifle manufactured by Burrell Defense",
        "name": "D-2 Double Take",
        "nameshort": "doubletake",
        "class": "pilot_primary",
        "type": "sniper",
    }

    EPG = {
        "desc": "Single fire, direct energy propelled launcher.",
        "longdesc": "The EPG-1, or Energy Propelled Grenade, is an advanced plasma antipersonnel grenade launcher appearing in Titanfall 2. It fires slow-moving blue plasma grenades with high splash damage.",
        "name": "EPG-1",
        "nameshort": "epg",
        "class": "pilot_primary",
        "type": "grenadier",
    }

    EVA8 = {
        "desc": "Fully automatic shotgun.",
        "longdesc": "The EVA-8 (Extra-Vehicular Activity) Automatic Shotgun is a Pilot anti-personnel auto-loading shotgun manufactured by Wonyeon Defense.",
        "name": "EVA-8 Auto",
        "nameshort": "eva8",
        "class": "pilot_primary",
        "type": "shotgun",
    }

    FLATLINE = {
        "desc": "Full-auto with a punch.",
        "longdesc": "The V-47 Flatline is a Pilot anti-personnel fully automatic bullpup assault rifle, manufactured by Wonyeon Defense. It has negligible vertical recoil, instead involving an extreme degree of horizontal recoil, similar to the Alternator.",
        "name": "V-47 Flatline",
        "nameshort": "flatline",
        "class": "pilot_primary",
        "type": "assault_rifle",
    }

    G2A5 = {
        "desc": "Semi-auto precision rifle.",
        "longdesc": "The G2A5 is a semiautomatic battle rifle manufactured by Lastimosa Armory and the successor to the G2A4 Battle Rifle. It is a Pilot primary weapon with perfect accuracy.",
        "name": "G2A5",
        "nameshort": "g2a5",
        "class": "pilot_primary",
        "type": "assault_rifle",
    }

    HEMLOK = {
        "desc": "Burst-fire assault rifle.",
        "longdesc": "The M1A3 Hemlok BF-R (Burst-Fire Rifle) is a Pilot anti-personnel burst fire assault rifle.",
        "name": "Hemlok BF-R",
        "nameshort": "hemlok",
        "class": "pilot_primary",
        "type": "assault_rifle",
    }

    KRABER = {
        "desc": "Scoped heavy rifle.",
        "longdesc": "The Kraber-AP (Armor Penetrating) 14.5x114mm Sniper Rifle is a Pilot anti-personnel bolt-action heavy sniper rifle. It is manufactured by Lastimosa Armory.",
        "name": "Kraber-AP Sniper",
        "nameshort": "kraber",
        "class": "pilot_primary",
        "type": "sniper",
    }

    LEADWALL = {
        "desc": "Projectile shotgun with a wide spread.",
        "longdesc": "The Leadwall is the primary Titan weapon for Ronin in Titanfall 2. It is a shotgun, based on the same design as the Triple Threat grenade launcher of Titanfall.",
        "name": "Leadwall",
        "nameshort": "leadwall",
        "class": "titan_primary",
        "type": "titan_primary",
    }

    LONGBOW = {
        "desc": "Semi-auto sniper.",
        "longdesc": "The D-101 Longbow-DMR (Designated Marksman Rifle) Sniper Rifle is a Pilot anti-personnel semi-automatic sniper rifle manufactured by Lastimosa Armory. The DMR is a variant of the R-101 Assault Rifle, modified into a marksman rifle role.",
        "name": "Longbow-DMR",
        "nameshort": "longbow",
        "class": "pilot_primary",
        "type": "sniper",
    }

    LSTAR = {
        "desc": "Rapid fire energy LMG.",
        "longdesc": "The L-STAR (Lastimosa Armory Assault Rifle) is a Pilot anti-personnel fully automatic particle accelerating light machine gun manufactured by Lastimosa Armory.",
        "name": "L-STAR",
        "nameshort": "lstar",
        "class": "pilot_primary",
        "type": "lmg",
    }

    MASTIFF = {
        "desc": "Auto-loading shotgun with wide spread.",
        "longdesc": "The M1901 Mastiff Combat Shotgun is a Pilot anti-personnel energy semi-automatic shotgun manufactured by Lastimosa Armory.",
        "name": "Mastiff",
        "nameshort": "mastiff",
        "class": "pilot_primary",
        "type": "shotgun",
    }

    MGL = {
        "desc": "Magnetic grenade launcher.",
        "longdesc": "The MGL , also known as the Mag Launcher or Magnetic Grenade Launcher, is a Pilot anti-Titan magnetic grenade launcher manufactured by Wonyeon Defense.",
        "name": "MGL Mag Launcher",
        "nameshort": "mgl",
        "class": "pilot_at",
        "type": "grenadier",
    }

    MOZAMBIQUE = {
        "desc": "Controlled spread triple barrel shotgun pistol.",
        "longdesc": "The SA-3 Mozambique, also knowns as the Mozambique Shotgun is a Pilot anti-personnel, triple-barreled shotgun pistol.",
        "name": "SA-3 Mozambique",
        "nameshort": "mozambique",
        "class": "pilot_pistol",
        "type": "pistol",
    }

    P2016 = {
        "desc": "Precision semi-auto pistol.",
        "longdesc": "The Hammond P2016 is a sidearm manufactured by Lastimosa Armory. Like its predecessor, the P2016 is a Semi-Automatic Handgun.",
        "name": "Hammond P2016",
        "nameshort": "p2016",
        "class": "pilot_pistol",
        "type": "pistol",
    }

    SPLITTER = {
        "desc": "Drains energy to split the shot, increasing damage",
        "longdesc": "The Splitter Rifle (Otherwise known as the Titan Particle Accelerator or TPAR)is a Titan fully-automatic energy rifle",
        "name": "Splitter Rifle",
        "nameshort": "splitter",
        "class": "titan_primary",
        "type": "titan_primary",
    }

    PREDATOR = {
        "desc": "Heavy minigun",
        "longdesc": "Powerful minigun with a long spin-up time.",
        "name": "Predator Cannon",
        "nameshort": "predator",
        "class": "titan_primary",
        "type": "titan_primary",
    }

    R101 = {
        "desc": "Factory issue scoped predecessor of the R-201 rifle.",
        "longdesc": "The R-101C (Compact) Carbine is a Pilot anti-personnel fully automatic carbine manufactured by Lastimosa Armory.",
        "name": "R-101 Carbine",
        "nameshort": "r101",
        "class": "pilot_primary",
        "type": "assault_rifle",
    }

    R201 = {
        "desc": "Full-auto and high accuracy.",
        "longdesc": "The R-201 Special Operations Assault Rifle (SOAR) is a Pilot anti-personnel fully automatic assault rifle manufactured by Lastimosa Armory, serving as the successor to the R-101C Carbine and the predecessor to the R-301 Carbine.",
        "name": "R-201 Carbine",
        "nameshort": "r201",
        "class": "pilot_primary",
        "type": "assault_rifle",
    }

    R97 = {
        "desc": "Rapid fire SMG.",
        "longdesc": "The R-97 Compact Submachine Gun (SMG) is a Pilot anti-personnel close-quarter submachine gun manufactured by Lastimosa Armory.",
        "name": "R-97",
        "nameshort": "r97",
        "class": "pilot_primary",
        "type": "smg",
    }

    RAILGUN = {
        "desc": "Charges up while zoomed.",
        "longdesc": "Sniper railgun that charges up while zoomed.",
        "name": "Plasma Railgun",
        "nameshort": "railgun",
        "class": "titan_primary",
        "type": "titan_primary",
    }

    RE45 = {
        "desc": ".45 cal full-auto pistol.",
        "longdesc": "The RE-45 Autopistol is a Pilot anti-personnel fully automatic machine pistol, manufactured by Lastimosa Armory and Paradinha Arsenal. It serves as a reliable 'spray-and-pray' backup sidearm for pilots at close range.",
        "name": "REEEEEEEE",
        "nameshort": "re45",
        "class": "pilot_pistol",
        "type": "pistol",
    }

    MK6 = {
        "desc": "Idiot pistol",
        "longdesc": "The next generation in AI targeting technology comes in the form of the Lastimosa Armory Smart Pistol MK6. Upgrades from the MK5 include a reciprocating charging handle, frame integrated ammo counter, multi-function Laser Aiming Module (LAM), etc.",
        "name": "Smart Pistol MK6",
        "nameshort": "mk6",
        "class": "pilot_pistol",
        "type": "pistol",
    }

    SMR = {
        "desc": "Rapidly fires micro-missiles.",
        "longdesc": "The Anti-Titan Sidewinder Micro Rocket launcher (AT-SMR), is an Anti-Titan Automatic Rocket Launcher (AT-ARL). It is manufactured by Wonyeon Defense.",
        "name": "Sidewinder SMR",
        "nameshort": "smr",
        "class": "pilot_at",
        "type": "anti_titan",
    }

    SOFTBALL = {
        "desc": "Adhesive grenade launcher.",
        "longdesc": "The R-6P Softball Anti-Armor Grenade Launcher (AAGL) is a Pilot anti-Titan/personnel grenade launcher",
        "name": "R-6P Softball",
        "nameshort": "softball",
        "class": "pilot_primary",
        "type": "grenadier",
    }

    SPITFIRE = {
        "desc": "Steady fire rate with a punch.",
        "longdesc": "The Spitfire Light Machine Gun (LMG) is a Pilot anti-personnel fully automatic light machine gun.",
        "name": "Spitfire",
        "nameshort": "spitfire",
        "class": "pilot_primary",
        "type": "lmg",
    }

    T203 = {
        "desc": "Ignites the impact area.",
        "longdesc": "Giant thermite grenades ignite the impact area.",
        "name": "T-203 Thermite Launcher",
        "nameshort": "t203",
        "class": "titan_primary",
        "type": "titan_primary",
    }

    THR40MM = {
        "desc": "Semi-auto 40mm HE rounds.",
        "longdesc": "The factory issue 40mm Cannon is a semi-automatic weapon that fires a high-explosive round with good accuracy.",
        "name": "40mm Cannon",
        "nameshort": "thr40mm",
        "class": "titan_primary",
        "type": "titan_primary",
    }

    THUNDERBOLT = {
        "desc": "Fires a powerful ball of electricity.",
        "longdesc": "The LG-97 Thunderbolt is a Pilot anti-Titan energy projector that fires a large, slow-moving ball of electricity that causes damage to any unit within a wide radius around its flight path. Upon striking a target, it explodes in a spherical blast.",
        "name": "LG-97 Thunderbolt",
        "nameshort": "thunderbolt",
        "class": "pilot_at",
        "type": "anti_titan",
    }

    VOLT = {
        "desc": "Energy actuated SMG.",
        "longdesc": "The Volt is a Pilot energy submachine gun. It is a weapon that fires concentrated bolts of high energy, which are referred to as 'blue tracers'.",
        "name": "Volt",
        "nameshort": "volt",
        "class": "pilot_primary",
        "type": "smg",
    }

    WINGMAN = {
        "desc": "High-powered revolver.",
        "longdesc": "The B3 Wingman is a Pilot anti-personnel revolver handgun sidearm. The Wingman boasts immense high-caliber stopping power and notable accuracy to compensate for its small magazine and relatively slow fire rate.",
        "name": "B3 Wingman",
        "nameshort": "wingman",
        "class": "pilot_pistol",
        "type": "pistol",
    }

    WINGMANN = {
        "desc": "Extended range projectile pistol with stock scope.",
        "longdesc": "Bish's personal and most trusted sidearm. The B3 Wingman Elite has been customized to fit the needs of an inter-colonial arms dealer with a shady past and even cloudier business practices.",
        "name": "Wingman Elite",
        "nameshort": "wingmann",
        "class": "pilot_pistol",
        "type": "pistol",
    }

    CHAINGUN = {
        "desc": "20mm automatic rifle.",
        "longdesc": "20mm automatic rifle.",
        "name": "XO-16",
        "nameshort": "chaingun",
        "class": "titan_primary",
        "type": "titan_primary",
    }

tracing_start()
start = time.time()


list = {
    "alternator": {
        "desc": FRONTEND.ALTERNATOR["desc"],
        "longdesc": FRONTEND.ALTERNATOR["longdesc"],
        "name": FRONTEND.ALTERNATOR["name"],
        "nameshort": FRONTEND.ALTERNATOR["nameshort"],
        "class": FRONTEND.ALTERNATOR["class"],
        "type": FRONTEND.ALTERNATOR["type"],
    },
    "archer": {
        "desc": FRONTEND.ARCHER["desc"],
        "longdesc": FRONTEND.ARCHER["longdesc"],
        "name": FRONTEND.ARCHER["name"],
        "nameshort": FRONTEND.ARCHER["nameshort"],
        "class": FRONTEND.ARCHER["class"],
        "type": FRONTEND.ARCHER["type"],
    },
    "car": {
        "desc": FRONTEND.CAR["desc"],
        "longdesc": FRONTEND.CAR["longdesc"],
        "name": FRONTEND.CAR["name"],
        "nameshort": FRONTEND.CAR["nameshort"],
        "class": FRONTEND.CAR["class"],
        "type": FRONTEND.CAR["type"],
    },
    "coldwar": {
        "desc": FRONTEND.COLDWAR["desc"],
        "longdesc": FRONTEND.COLDWAR["longdesc"],
        "name": FRONTEND.COLDWAR["name"],
        "nameshort": FRONTEND.COLDWAR["nameshort"],
        "class": FRONTEND.COLDWAR["class"],
        "type": FRONTEND.COLDWAR["type"],
    },
    "defender": {
        "desc": FRONTEND.DEFENDER["desc"],
        "longdesc": FRONTEND.DEFENDER["longdesc"],
        "name": FRONTEND.DEFENDER["name"],
        "nameshort": FRONTEND.DEFENDER["nameshort"],
        "class": FRONTEND.DEFENDER["class"],
        "type": FRONTEND.DEFENDER["type"],
    },
    "devotion": {
        "desc": FRONTEND.DEVOTION["desc"],
        "longdesc": FRONTEND.DEVOTION["longdesc"],
        "name": FRONTEND.DEVOTION["name"],
        "nameshort": FRONTEND.DEVOTION["nameshort"],
        "class": FRONTEND.DEVOTION["class"],
        "type": FRONTEND.DEVOTION["type"],
    },
    "doubletake": {
        "desc": FRONTEND.DOUBLETAKE["desc"],
        "longdesc": FRONTEND.DOUBLETAKE["longdesc"],
        "name": FRONTEND.DOUBLETAKE["name"],
        "nameshort": FRONTEND.DOUBLETAKE["nameshort"],
        "class": FRONTEND.DOUBLETAKE["class"],
        "type": FRONTEND.DOUBLETAKE["type"],
    },
    "epg": {
        "desc": FRONTEND.EPG["desc"],
        "longdesc": FRONTEND.EPG["longdesc"],
        "name": FRONTEND.EPG["name"],
        "nameshort": FRONTEND.EPG["nameshort"],
        "class": FRONTEND.EPG["class"],
        "type": FRONTEND.EPG["type"],
    },
    "eva8": {
        "desc": FRONTEND.EVA8["desc"],
        "longdesc": FRONTEND.EVA8["longdesc"],
        "name": FRONTEND.EVA8["name"],
        "nameshort": FRONTEND.EVA8["nameshort"],
        "class": FRONTEND.EVA8["class"],
        "type": FRONTEND.EVA8["type"],
    },
    "flatline": {
        "desc": FRONTEND.FLATLINE["desc"],
        "longdesc": FRONTEND.FLATLINE["longdesc"],
        "name": FRONTEND.FLATLINE["name"],
        "nameshort": FRONTEND.FLATLINE["nameshort"],
        "class": FRONTEND.FLATLINE["class"],
        "type": FRONTEND.FLATLINE["type"],
    },
    "g2a5": {
        "desc": FRONTEND.G2A5["desc"],
        "longdesc": FRONTEND.G2A5["longdesc"],
        "name": FRONTEND.G2A5["name"],
        "nameshort": FRONTEND.G2A5["nameshort"],
        "class": FRONTEND.G2A5["class"],
        "type": FRONTEND.G2A5["type"],
    },
    "hemlok": {
        "desc": FRONTEND.HEMLOK["desc"],
        "longdesc": FRONTEND.HEMLOK["longdesc"],
        "name": FRONTEND.HEMLOK["name"],
        "nameshort": FRONTEND.HEMLOK["nameshort"],
        "class": FRONTEND.HEMLOK["class"],
        "type": FRONTEND.HEMLOK["type"],
    },
    "kraber": {
        "desc": FRONTEND.KRABER["desc"],
        "longdesc": FRONTEND.KRABER["longdesc"],
        "name": FRONTEND.KRABER["name"],
        "nameshort": FRONTEND.KRABER["nameshort"],
        "class": FRONTEND.KRABER["class"],
        "type": FRONTEND.KRABER["type"],
    },
    "leadwall": {
        "desc": FRONTEND.LEADWALL["desc"],
        "longdesc": FRONTEND.LEADWALL["longdesc"],
        "name": FRONTEND.LEADWALL["name"],
        "nameshort": FRONTEND.LEADWALL["nameshort"],
        "class": FRONTEND.LEADWALL["class"],
        "type": FRONTEND.LEADWALL["type"],
    },
    "longbow": {
        "desc": FRONTEND.LONGBOW["desc"],
        "longdesc": FRONTEND.LONGBOW["longdesc"],
        "name": FRONTEND.LONGBOW["name"],
        "nameshort": FRONTEND.LONGBOW["nameshort"],
        "class": FRONTEND.LONGBOW["class"],
        "type": FRONTEND.LONGBOW["type"],
    },
    "lstar": {
        "desc": FRONTEND.LSTAR["desc"],
        "longdesc": FRONTEND.LSTAR["longdesc"],
        "name": FRONTEND.LSTAR["name"],
        "nameshort": FRONTEND.LSTAR["nameshort"],
        "class": FRONTEND.LSTAR["class"],
        "type": FRONTEND.LSTAR["type"],
    },
    "mastiff": {
        "desc": FRONTEND.MASTIFF["desc"],
        "longdesc": FRONTEND.MASTIFF["longdesc"],
        "name": FRONTEND.MASTIFF["name"],
        "nameshort": FRONTEND.MASTIFF["nameshort"],
        "class": FRONTEND.MASTIFF["class"],
        "type": FRONTEND.MASTIFF["type"],
    },
    "mgl": {
        "desc": FRONTEND.MGL["desc"],
        "longdesc": FRONTEND.MGL["longdesc"],
        "name": FRONTEND.MGL["name"],
        "nameshort": FRONTEND.MGL["nameshort"],
        "class": FRONTEND.MGL["class"],
        "type": FRONTEND.MGL["type"],
    },
    "mozambique": {
        "desc": FRONTEND.MOZAMBIQUE["desc"],
        "longdesc": FRONTEND.MOZAMBIQUE["longdesc"],
        "name": FRONTEND.MOZAMBIQUE["name"],
        "nameshort": FRONTEND.MOZAMBIQUE["nameshort"],
        "class": FRONTEND.MOZAMBIQUE["class"],
        "type": FRONTEND.MOZAMBIQUE["type"],
    },
    "p2016": {
        "desc": FRONTEND.P2016["desc"],
        "longdesc": FRONTEND.P2016["longdesc"],
        "name": FRONTEND.P2016["name"],
        "nameshort": FRONTEND.P2016["nameshort"],
        "class": FRONTEND.P2016["class"],
        "type": FRONTEND.P2016["type"],
    },
    "splitter": {
        "desc": FRONTEND.SPLITTER["desc"],
        "longdesc": FRONTEND.SPLITTER["longdesc"],
        "name": FRONTEND.SPLITTER["name"],
        "nameshort": FRONTEND.SPLITTER["nameshort"],
        "class": FRONTEND.SPLITTER["class"],
        "type": FRONTEND.SPLITTER["type"],
    },
    "predator": {
        "desc": FRONTEND.PREDATOR["desc"],
        "longdesc": FRONTEND.PREDATOR["longdesc"],
        "name": FRONTEND.PREDATOR["name"],
        "nameshort": FRONTEND.PREDATOR["nameshort"],
        "class": FRONTEND.PREDATOR["class"],
        "type": FRONTEND.PREDATOR["type"],
    },
    "r101": {
        "desc": FRONTEND.R101["desc"],
        "longdesc": FRONTEND.R101["longdesc"],
        "name": FRONTEND.R101["name"],
        "nameshort": FRONTEND.R101["nameshort"],
        "class": FRONTEND.R101["class"],
        "type": FRONTEND.R101["type"],
    },
    "r201": {
        "desc": FRONTEND.R201["desc"],
        "longdesc": FRONTEND.R201["longdesc"],
        "name": FRONTEND.R201["name"],
        "nameshort": FRONTEND.R201["nameshort"],
        "class": FRONTEND.R201["class"],
        "type": FRONTEND.R201["type"],
    },
    "r97": {
        "desc": FRONTEND.R97["desc"],
        "longdesc": FRONTEND.R97["longdesc"],
        "name": FRONTEND.R97["name"],
        "nameshort": FRONTEND.R97["nameshort"],
        "class": FRONTEND.R97["class"],
        "type": FRONTEND.R97["type"],
    },
    "railgun": {
        "desc": FRONTEND.RAILGUN["desc"],
        "longdesc": FRONTEND.RAILGUN["longdesc"],
        "name": FRONTEND.RAILGUN["name"],
        "nameshort": FRONTEND.RAILGUN["nameshort"],
        "class": FRONTEND.RAILGUN["class"],
        "type": FRONTEND.RAILGUN["type"],
    },
    "re45": {
        "desc": FRONTEND.RE45["desc"],
        "longdesc": FRONTEND.RE45["longdesc"],
        "name": FRONTEND.RE45["name"],
        "nameshort": FRONTEND.RE45["nameshort"],
        "class": FRONTEND.RE45["class"],
        "type": FRONTEND.RE45["type"],
    },
    "mk6": {
        "desc": FRONTEND.MK6["desc"],
        "longdesc": FRONTEND.MK6["longdesc"],
        "name": FRONTEND.MK6["name"],
        "nameshort": FRONTEND.MK6["nameshort"],
        "class": FRONTEND.MK6["class"],
        "type": FRONTEND.MK6["type"],
    },
    "smr": {
        "desc": FRONTEND.SMR["desc"],
        "longdesc": FRONTEND.SMR["longdesc"],
        "name": FRONTEND.SMR["name"],
        "nameshort": FRONTEND.SMR["nameshort"],
        "class": FRONTEND.SMR["class"],
        "type": FRONTEND.SMR["type"],
    },
    "softball": {
        "desc": FRONTEND.SOFTBALL["desc"],
        "longdesc": FRONTEND.SOFTBALL["longdesc"],
        "name": FRONTEND.SOFTBALL["name"],
        "nameshort": FRONTEND.SOFTBALL["nameshort"],
        "class": FRONTEND.SOFTBALL["class"],
        "type": FRONTEND.SOFTBALL["type"],
    },
    "spitfire": {
        "desc": FRONTEND.SPITFIRE["desc"],
        "longdesc": FRONTEND.SPITFIRE["longdesc"],
        "name": FRONTEND.SPITFIRE["name"],
        "nameshort": FRONTEND.SPITFIRE["nameshort"],
        "class": FRONTEND.SPITFIRE["class"],
        "type": FRONTEND.SPITFIRE["type"],
    },
    "t203": {
        "desc": FRONTEND.T203["desc"],
        "longdesc": FRONTEND.T203["longdesc"],
        "name": FRONTEND.T203["name"],
        "nameshort": FRONTEND.T203["nameshort"],
        "class": FRONTEND.T203["class"],
        "type": FRONTEND.T203["type"],
    },
    "thr40mm": {
        "desc": FRONTEND.THR40MM["desc"],
        "longdesc": FRONTEND.THR40MM["longdesc"],
        "name": FRONTEND.THR40MM["name"],
        "nameshort": FRONTEND.THR40MM["nameshort"],
        "class": FRONTEND.THR40MM["class"],
        "type": FRONTEND.THR40MM["type"],
    },
    "thunderbolt": {
        "desc": FRONTEND.THUNDERBOLT["desc"],
        "longdesc": FRONTEND.THUNDERBOLT["longdesc"],
        "name": FRONTEND.THUNDERBOLT["name"],
        "nameshort": FRONTEND.THUNDERBOLT["nameshort"],
        "class": FRONTEND.THUNDERBOLT["class"],
        "type": FRONTEND.THUNDERBOLT["type"],
    },
    "volt": {
        "desc": FRONTEND.VOLT["desc"],
        "longdesc": FRONTEND.VOLT["longdesc"],
        "name": FRONTEND.VOLT["name"],
        "nameshort": FRONTEND.VOLT["nameshort"],
        "class": FRONTEND.VOLT["class"],
        "type": FRONTEND.VOLT["type"],
    },
    "wingman": {
        "desc": FRONTEND.WINGMAN["desc"],
        "longdesc": FRONTEND.WINGMAN["longdesc"],
        "name": FRONTEND.WINGMAN["name"],
        "nameshort": FRONTEND.WINGMAN["nameshort"],
        "class": FRONTEND.WINGMAN["class"],
        "type": FRONTEND.WINGMAN["type"],
    },
    "wingmann": {
        "desc": FRONTEND.WINGMANN["desc"],
        "longdesc": FRONTEND.WINGMANN["longdesc"],
        "name": FRONTEND.WINGMANN["name"],
        "nameshort": FRONTEND.WINGMANN["nameshort"],
        "class": FRONTEND.WINGMANN["class"],
        "type": FRONTEND.WINGMANN["type"],
    },
    "chaingun": {
        "desc": FRONTEND.CHAINGUN["desc"],
        "longdesc": FRONTEND.CHAINGUN["longdesc"],
        "name": FRONTEND.CHAINGUN["name"],
        "nameshort": FRONTEND.CHAINGUN["nameshort"],
        "class": FRONTEND.CHAINGUN["class"],
        "type": FRONTEND.CHAINGUN["type"],
    },
}

print(list)
print()
print()
print()
print()

end = time.time()
print("time elapsed {} milli seconds".format((end-start)*1000))
tracing_mem()
