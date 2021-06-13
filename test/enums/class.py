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
    WPN_ALTERNATOR_DESC = "Twin Barrel SMG."
    WPN_ALTERNATOR_LONGDESC = "The Alternator (also referred to as the SP-14 Hatchet in concept art) is a Pilot anti-personnel twin-barrel submachine gun manufactured by Emslie Tactical."
    WPN_ALTERNATOR_NAME = "Alternator"
    WPN_ALTERNATOR_NAME_SHORT = "alternator"
    WPN_ALTERNATOR_CLASS = "pilot_primary"
    WPN_ALTERNATOR_TYPE = "smg"

    WPN_ARCHER_DESC = "Rocket Launcher with Anti-Titan lock-on."
    WPN_ARCHER_LONGDESC = "The Archer Heavy Rocket, also known simply as the Archer, is an anti-Titan lock-on rocket launcher manufactured by Brockhaurd Manufacturing."
    WPN_ARCHER_NAME = "Archer"
    WPN_ARCHER_NAME_SHORT = "archer"
    WPN_ARCHER_CLASS = "pilot_at"
    WPN_ARCHER_TYPE = "anti_titan"

    WPN_CAR_DESC = "Consistent recoil SMG."
    WPN_CAR_LONGDESC = "The Combat Advanced Round Submachine Gun (C.A.R. SMG) is a Pilot anti-personnel fully automatic submachine gun that appears in Titanfall and Titanfall 2"
    WPN_CAR_NAME = "CAR"
    WPN_CAR_NAME_SHORT = "car"
    WPN_CAR_CLASS = "pilot_primary"
    WPN_CAR_TYPE = "smg"

    WPN_COLDWAR_DESC = "4-round burst Grenadier weapon."
    WPN_COLDWAR_LONGDESC = "The EM-4 Cold War is a primary four-round burst bullpup grenade launcher manufactured by Vinson Dynamics, firing 4.73x33mm explosive ammunition."
    WPN_COLDWAR_NAME = "EM-4 Cold War"
    WPN_COLDWAR_NAME_SHORT = "coldwar"
    WPN_COLDWAR_CLASS = "pilot_primary"
    WPN_COLDWAR_TYPE = "grenadier"

    WPN_DEFENDER_DESC = "Charged precision beam Anti-Titan sniper."
    WPN_DEFENDER_LONGDESC = "The Charge Rifle fires an energy beam that inflicts massive damage. Holding the trigger charges the weapon."
    WPN_DEFENDER_NAME = "Charge Rifle"
    WPN_DEFENDER_NAME_SHORT = "defender"
    WPN_DEFENDER_CLASS = "pilot_at"
    WPN_DEFENDER_TYPE = "anti_titan"

    WPN_DEVOTION_DESC = "Ramps up fire rate over time."
    WPN_DEVOTION_LONGDESC = "The X-55 Devotion is a light machine guns (LMGs). Its fire rate increases greatly the longer the trigger is held."
    WPN_DEVOTION_NAME = "X-55 Devotion"
    WPN_DEVOTION_NAME_SHORT = "devotion"
    WPN_DEVOTION_CLASS = "pilot_primary"
    WPN_DEVOTION_TYPE = "lmg"

    WPN_DOUBLETAKE_DESC = "Twin-fire sniper rifle."
    WPN_DOUBLETAKE_LONGDESC = "The D-2 Double Take is a Pilot anti-personnel semi-automatic twin-barrel bullpup marksman rifle manufactured by Burrell Defense"
    WPN_DOUBLETAKE_NAME = "D-2 Double Take"
    WPN_DOUBLETAKE_NAME_SHORT = "doubletake"
    WPN_DOUBLETAKE_CLASS = "pilot_primary"
    WPN_DOUBLETAKE_TYPE = "sniper"

    WPN_EPG_DESC = "Single fire, direct energy propelled launcher."
    WPN_EPG_LONGDESC = "The EPG-1, or Energy Propelled Grenade, is an advanced plasma antipersonnel grenade launcher appearing in Titanfall 2. It fires slow-moving blue plasma grenades with high splash damage."
    WPN_EPG_NAME = "EPG-1"
    WPN_EPG_NAME_SHORT = "epg"
    WPN_EPG_CLASS = "pilot_primary"
    WPN_EPG_TYPE = "grenadier"

    WPN_EVA8_DESC = "Fully automatic shotgun."
    WPN_EVA8_LONGDESC = "The EVA-8 (Extra-Vehicular Activity) Automatic Shotgun is a Pilot anti-personnel auto-loading shotgun manufactured by Wonyeon Defense."
    WPN_EVA8_NAME = "EVA-8 Auto"
    WPN_EVA8_NAME_SHORT = "eva8"
    WPN_EVA8_CLASS = "pilot_primary"
    WPN_EVA8_TYPE = "shotgun"

    WPN_FLATLINE_DESC = "Full-auto with a punch."
    WPN_FLATLINE_LONGDESC = "The V-47 Flatline is a Pilot anti-personnel fully automatic bullpup assault rifle, manufactured by Wonyeon Defense. It has negligible vertical recoil, instead involving an extreme degree of horizontal recoil, similar to the Alternator."
    WPN_FLATLINE_NAME = "V-47 Flatline"
    WPN_FLATLINE_NAME_SHORT = "flatline"
    WPN_FLATLINE_CLASS = "pilot_primary"
    WPN_FLATLINE_TYPE = "assault_rifle"

    WPN_G2A5_DESC = "Semi-auto precision rifle."
    WPN_G2A5_LONGDESC = "The G2A5 is a semiautomatic battle rifle manufactured by Lastimosa Armory and the successor to the G2A4 Battle Rifle. It is a Pilot primary weapon with perfect accuracy."
    WPN_G2A5_NAME = "G2A5"
    WPN_G2A5_NAME_SHORT = "g2a5"
    WPN_G2A5_CLASS = "pilot_primary"
    WPN_G2A5_TYPE = "assault_rifle"

    WPN_HEMLOK_DESC = "Burst-fire assault rifle."
    WPN_HEMLOK_LONGDESC = "The M1A3 Hemlok BF-R (Burst-Fire Rifle) is a Pilot anti-personnel burst fire assault rifle."
    WPN_HEMLOK_NAME = "Hemlok BF-R"
    WPN_HEMLOK_NAME_SHORT = "hemlok"
    WPN_HEMLOK_CLASS = "pilot_primary"
    WPN_HEMLOK_TYPE = "assault_rifle"

    WPN_KRABER_DESC = "Scoped heavy rifle."
    WPN_KRABER_LONGDESC = "The Kraber-AP (Armor Penetrating) 14.5x114mm Sniper Rifle is a Pilot anti-personnel bolt-action heavy sniper rifle. It is manufactured by Lastimosa Armory."
    WPN_KRABER_NAME = "Kraber-AP Sniper"
    WPN_KRABER_NAME_SHORT = "kraber"
    WPN_KRABER_CLASS = "pilot_primary"
    WPN_KRABER_TYPE = "sniper"

    WPN_LEADWALL_DESC = "Projectile shotgun with a wide spread."
    WPN_LEADWALL_LONGDESC = "The Leadwall is the primary Titan weapon for Ronin in Titanfall 2. It is a shotgun, based on the same design as the Triple Threat grenade launcher of Titanfall."
    WPN_LEADWALL_NAME = "Leadwall"
    WPN_LEADWALL_NAME_SHORT = "leadwall"
    WPN_LEADWALL_CLASS = "titan_primary"
    WPN_LEADWALL_TYPE = "titan_primary"

    WPN_LONGBOW_DESC = "Semi-auto sniper."
    WPN_LONGBOW_LONGDESC = "The D-101 Longbow-DMR (Designated Marksman Rifle) Sniper Rifle is a Pilot anti-personnel semi-automatic sniper rifle manufactured by Lastimosa Armory. The DMR is a variant of the R-101 Assault Rifle, modified into a marksman rifle role."
    WPN_LONGBOW_NAME = "Longbow-DMR"
    WPN_LONGBOW_NAME_SHORT = "longbow"
    WPN_LONGBOW_CLASS = "pilot_primary"
    WPN_LONGBOW_TYPE = "sniper"

    WPN_LSTAR_DESC = "Rapid fire energy LMG."
    WPN_LSTAR_LONGDESC = "The L-STAR (Lastimosa Armory Assault Rifle) is a Pilot anti-personnel fully automatic particle accelerating light machine gun manufactured by Lastimosa Armory."
    WPN_LSTAR_NAME = "L-STAR"
    WPN_LSTAR_NAME_SHORT = "lstar"
    WPN_LSTAR_CLASS = "pilot_primary"
    WPN_LSTAR_TYPE = "lmg"

    WPN_MASTIFF_DESC = "Auto-loading shotgun with wide spread."
    WPN_MASTIFF_LONGDESC = "The M1901 Mastiff Combat Shotgun is a Pilot anti-personnel energy semi-automatic shotgun manufactured by Lastimosa Armory."
    WPN_MASTIFF_NAME = "Mastiff"
    WPN_MASTIFF_NAME_SHORT = "mastiff"
    WPN_MASTIFF_CLASS = "pilot_primary"
    WPN_MASTIFF_TYPE = "shotgun"

    WPN_MGL_DESC = "Magnetic grenade launcher."
    WPN_MGL_LONGDESC = "The MGL , also known as the Mag Launcher or Magnetic Grenade Launcher, is a Pilot anti-Titan magnetic grenade launcher manufactured by Wonyeon Defense."
    WPN_MGL_NAME = "MGL Mag Launcher"
    WPN_MGL_NAME_SHORT = "mgl"
    WPN_MGL_CLASS = "pilot_at"
    WPN_MGL_TYPE = "grenadier"

    WPN_MOZAMBIQUE_DESC = "Controlled spread triple barrel shotgun pistol."
    WPN_MOZAMBIQUE_LONGDESC = "The SA-3 Mozambique, also knowns as the Mozambique Shotgun is a Pilot anti-personnel, triple-barreled shotgun pistol."
    WPN_MOZAMBIQUE_NAME = "SA-3 Mozambique"
    WPN_MOZAMBIQUE_NAME_SHORT = "mozambique"
    WPN_MOZAMBIQUE_CLASS = "pilot_pistol"
    WPN_MOZAMBIQUE_TYPE = "pistol"

    WPN_P2016_DESC = "Precision semi-auto pistol."
    WPN_P2016_LONGDESC = "The Hammond P2016 is a sidearm manufactured by Lastimosa Armory. Like its predecessor, the P2016 is a Semi-Automatic Handgun."
    WPN_P2016_NAME = "Hammond P2016"
    WPN_P2016_NAME_SHORT = "p2016"
    WPN_P2016_CLASS = "pilot_pistol"
    WPN_P2016_TYPE = "pistol"

    WPN_SPLITTER_DESC = "Drains energy to split the shot, increasing damage"
    WPN_SPLITTER_LONGDESC = "The Splitter Rifle (Otherwise known as the Titan Particle Accelerator or TPAR)is a Titan fully-automatic energy rifle"
    WPN_SPLITTER_NAME = "Splitter Rifle"
    WPN_SPLITTER_NAME_SHORT = "splitter"
    WPN_SPLITTER_CLASS = "titan_primary"
    WPN_SPLITTER_TYPE = "titan_primary"

    WPN_PREDATOR_DESC = "Heavy minigun"
    WPN_PREDATOR_LONGDESC = "Powerful minigun with a long spin-up time."
    WPN_PREDATOR_NAME = "Predator Cannon"
    WPN_PREDATOR_NAME_SHORT = "predator"
    WPN_PREDATOR_CLASS = "titan_primary"
    WPN_PREDATOR_TYPE = "titan_primary"

    WPN_R101_DESC = "Factory issue scoped predecessor of the R-201 rifle."
    WPN_R101_LONGDESC = "The R-101C (Compact) Carbine is a Pilot anti-personnel fully automatic carbine manufactured by Lastimosa Armory."
    WPN_R101_NAME = "R-101 Carbine"
    WPN_R101_NAME_SHORT = "r101"
    WPN_R101_CLASS = "pilot_primary"
    WPN_R101_TYPE = "assault_rifle"

    WPN_R201_DESC = "Full-auto and high accuracy."
    WPN_R201_LONGDESC = "The R-201 Special Operations Assault Rifle (SOAR) is a Pilot anti-personnel fully automatic assault rifle manufactured by Lastimosa Armory, serving as the successor to the R-101C Carbine and the predecessor to the R-301 Carbine."
    WPN_R201_NAME = "R-201 Carbine"
    WPN_R201_NAME_SHORT = "r201"
    WPN_R201_CLASS = "pilot_primary"
    WPN_R201_TYPE = "assault_rifle"

    WPN_R97_DESC = "Rapid fire SMG."
    WPN_R97_LONGDESC = "The R-97 Compact Submachine Gun (SMG) is a Pilot anti-personnel close-quarter submachine gun manufactured by Lastimosa Armory."
    WPN_R97_NAME = "R-97"
    WPN_R97_NAME_SHORT = "r97"
    WPN_R97_CLASS = "pilot_primary"
    WPN_R97_TYPE = "smg"

    WPN_RAILGUN_DESC = "Charges up while zoomed."
    WPN_RAILGUN_LONGDESC = "Sniper railgun that charges up while zoomed."
    WPN_RAILGUN_NAME = "Plasma Railgun"
    WPN_RAILGUN_NAME_SHORT = "railgun"
    WPN_RAILGUN_CLASS = "titan_primary"
    WPN_RAILGUN_TYPE = "titan_primary"

    WPN_RE45_DESC = ".45 cal full-auto pistol."
    WPN_RE45_LONGDESC = "The RE-45 Autopistol is a Pilot anti-personnel fully automatic machine pistol, manufactured by Lastimosa Armory and Paradinha Arsenal. It serves as a reliable 'spray-and-pray' backup sidearm for pilots at close range."
    WPN_RE45_NAME = "REEEEEEEE"
    WPN_RE45_NAME_SHORT = "re45"
    WPN_RE45_CLASS = "pilot_pistol"
    WPN_RE45_TYPE = "pistol"

    WPN_MK6_DESC = "Idiot pistol"
    WPN_MK6_LONGDESC = "The next generation in AI targeting technology comes in the form of the Lastimosa Armory Smart Pistol MK6. Upgrades from the MK5 include a reciprocating charging handle, frame integrated ammo counter, multi-function Laser Aiming Module (LAM), etc."
    WPN_MK6_NAME = "Smart Pistol MK6"
    WPN_MK6_NAME_SHORT = "mk6"
    WPN_MK6_CLASS = "pilot_pistol"
    WPN_MK6_TYPE = "pistol"

    WPN_SMR_DESC = "Rapidly fires micro-missiles."
    WPN_SMR_LONGDESC = "The Anti-Titan Sidewinder Micro Rocket launcher (AT-SMR), is an Anti-Titan Automatic Rocket Launcher (AT-ARL). It is manufactured by Wonyeon Defense."
    WPN_SMR_NAME = "Sidewinder SMR"
    WPN_SMR_NAME_SHORT = "smr"
    WPN_SMR_CLASS = "pilot_at"
    WPN_SMR_TYPE = "anti_titan"

    WPN_SOFTBALL_DESC = "Adhesive grenade launcher."
    WPN_SOFTBALL_LONGDESC = "The R-6P Softball Anti-Armor Grenade Launcher (AAGL) is a Pilot anti-Titan/personnel grenade launcher"
    WPN_SOFTBALL_NAME = "R-6P Softball"
    WPN_SOFTBALL_NAME_SHORT = "softball"
    WPN_SOFTBALL_CLASS = "pilot_primary"
    WPN_SOFTBALL_TYPE = "grenadier"

    WPN_SPITFIRE_DESC = "Steady fire rate with a punch."
    WPN_SPITFIRE_LONGDESC = "The Spitfire Light Machine Gun (LMG) is a Pilot anti-personnel fully automatic light machine gun."
    WPN_SPITFIRE_NAME = "Spitfire"
    WPN_SPITFIRE_NAME_SHORT = "spitfire"
    WPN_SPITFIRE_CLASS = "pilot_primary"
    WPN_SPITFIRE_TYPE = "lmg"

    WPN_T203_DESC = "Ignites the impact area."
    WPN_T203_LONGDESC = "Giant thermite grenades ignite the impact area."
    WPN_T203_NAME = "T-203 Thermite Launcher"
    WPN_T203_NAME_SHORT = "t203"
    WPN_T203_CLASS = "titan_primary"
    WPN_T203_TYPE = "titan_primary"

    WPN_THR40MM_DESC = "Semi-auto 40mm HE rounds."
    WPN_THR40MM_LONGDESC = "The factory issue 40mm Cannon is a semi-automatic weapon that fires a high-explosive round with good accuracy."
    WPN_THR40MM_NAME = "40mm Cannon"
    WPN_THR40MM_NAME_SHORT = "thr40mm"
    WPN_THR40MM_CLASS = "titan_primary"
    WPN_THR40MM_TYPE = "titan_primary"

    WPN_THUNDERBOLT_DESC = "Fires a powerful ball of electricity."
    WPN_THUNDERBOLT_LONGDESC = "The LG-97 Thunderbolt is a Pilot anti-Titan energy projector that fires a large, slow-moving ball of electricity that causes damage to any unit within a wide radius around its flight path. Upon striking a target, it explodes in a spherical blast."
    WPN_THUNDERBOLT_NAME = "LG-97 Thunderbolt"
    WPN_THUNDERBOLT_NAME_SHORT = "thunderbolt"
    WPN_THUNDERBOLT_CLASS = "pilot_at"
    WPN_THUNDERBOLT_TYPE = "anti_titan"

    WPN_VOLT_DESC = "Energy actuated SMG."
    WPN_VOLT_LONGDESC = "The Volt is a Pilot energy submachine gun. It is a weapon that fires concentrated bolts of high energy, which are referred to as 'blue tracers'."
    WPN_VOLT_NAME = "Volt"
    WPN_VOLT_NAME_SHORT = "volt"
    WPN_VOLT_CLASS = "pilot_primary"
    WPN_VOLT_TYPE = "smg"

    WPN_WINGMAN_DESC = "High-powered revolver."
    WPN_WINGMAN_LONGDESC = "The B3 Wingman is a Pilot anti-personnel revolver handgun sidearm. The Wingman boasts immense high-caliber stopping power and notable accuracy to compensate for its small magazine and relatively slow fire rate."
    WPN_WINGMAN_NAME = "B3 Wingman"
    WPN_WINGMAN_NAME_SHORT = "wingman"
    WPN_WINGMAN_CLASS = "pilot_pistol"
    WPN_WINGMAN_TYPE = "pistol"

    WPN_WINGMANN_DESC = "Extended range projectile pistol with stock scope."
    WPN_WINGMANN_LONGDESC = "Bish's personal and most trusted sidearm. The B3 Wingman Elite has been customized to fit the needs of an inter-colonial arms dealer with a shady past and even cloudier business practices."
    WPN_WINGMANN_NAME = "Wingman Elite"
    WPN_WINGMANN_NAME_SHORT = "wingmann"
    WPN_WINGMANN_CLASS = "pilot_pistol"
    WPN_WINGMANN_TYPE = "pistol"

    WPN_CHAINGUN_DESC = "20mm automatic rifle."
    WPN_CHAINGUN_LONGDESC = "20mm automatic rifle."
    WPN_CHAINGUN_NAME = "XO-16"
    WPN_CHAINGUN_NAME_SHORT = "chaingun"
    WPN_CHAINGUN_CLASS = "titan_primary"
    WPN_CHAINGUN_TYPE = "titan_primary"

tracing_start()
start = time.time()


list = {
    "alternator": {
        "desc": FRONTEND.WPN_ALTERNATOR_DESC,
        "longdesc": FRONTEND.WPN_ALTERNATOR_LONGDESC,
        "name": FRONTEND.WPN_ALTERNATOR_NAME,
        "nameshort": FRONTEND.WPN_ALTERNATOR_NAME_SHORT,
        "class": FRONTEND.WPN_ALTERNATOR_CLASS,
        "type": FRONTEND.WPN_ALTERNATOR_TYPE,
    },
    "archer": {
        "desc": FRONTEND.WPN_ARCHER_DESC,
        "longdesc": FRONTEND.WPN_ARCHER_LONGDESC,
        "name": FRONTEND.WPN_ARCHER_NAME,
        "nameshort": FRONTEND.WPN_ARCHER_NAME_SHORT,
        "class": FRONTEND.WPN_ARCHER_CLASS,
        "type": FRONTEND.WPN_ARCHER_TYPE,
    },
    "car": {
        "desc": FRONTEND.WPN_CAR_DESC,
        "longdesc": FRONTEND.WPN_CAR_LONGDESC,
        "name": FRONTEND.WPN_CAR_NAME,
        "nameshort": FRONTEND.WPN_CAR_NAME_SHORT,
        "class": FRONTEND.WPN_CAR_CLASS,
        "type": FRONTEND.WPN_CAR_TYPE,
    },
    "coldwar": {
        "desc": FRONTEND.WPN_COLDWAR_DESC,
        "longdesc": FRONTEND.WPN_COLDWAR_LONGDESC,
        "name": FRONTEND.WPN_COLDWAR_NAME,
        "nameshort": FRONTEND.WPN_COLDWAR_NAME_SHORT,
        "class": FRONTEND.WPN_COLDWAR_CLASS,
        "type": FRONTEND.WPN_COLDWAR_TYPE,
    },
    "defender": {
        "desc": FRONTEND.WPN_DEFENDER_DESC,
        "longdesc": FRONTEND.WPN_DEFENDER_LONGDESC,
        "name": FRONTEND.WPN_DEFENDER_NAME,
        "nameshort": FRONTEND.WPN_DEFENDER_NAME_SHORT,
        "class": FRONTEND.WPN_DEFENDER_CLASS,
        "type": FRONTEND.WPN_DEFENDER_TYPE,
    },
    "devotion": {
        "desc": FRONTEND.WPN_DEVOTION_DESC,
        "longdesc": FRONTEND.WPN_DEVOTION_LONGDESC,
        "name": FRONTEND.WPN_DEVOTION_NAME,
        "nameshort": FRONTEND.WPN_DEVOTION_NAME_SHORT,
        "class": FRONTEND.WPN_DEVOTION_CLASS,
        "type": FRONTEND.WPN_DEVOTION_TYPE,
    },
    "doubletake": {
        "desc": FRONTEND.WPN_DOUBLETAKE_DESC,
        "longdesc": FRONTEND.WPN_DOUBLETAKE_LONGDESC,
        "name": FRONTEND.WPN_DOUBLETAKE_NAME,
        "nameshort": FRONTEND.WPN_DOUBLETAKE_NAME_SHORT,
        "class": FRONTEND.WPN_DOUBLETAKE_CLASS,
        "type": FRONTEND.WPN_DOUBLETAKE_TYPE,
    },
    "epg": {
        "desc": FRONTEND.WPN_EPG_DESC,
        "longdesc": FRONTEND.WPN_EPG_LONGDESC,
        "name": FRONTEND.WPN_EPG_NAME,
        "nameshort": FRONTEND.WPN_EPG_NAME_SHORT,
        "class": FRONTEND.WPN_EPG_CLASS,
        "type": FRONTEND.WPN_EPG_TYPE,
    },
    "eva8": {
        "desc": FRONTEND.WPN_EVA8_DESC,
        "longdesc": FRONTEND.WPN_EVA8_LONGDESC,
        "name": FRONTEND.WPN_EVA8_NAME,
        "nameshort": FRONTEND.WPN_EVA8_NAME_SHORT,
        "class": FRONTEND.WPN_EVA8_CLASS,
        "type": FRONTEND.WPN_EVA8_TYPE,
    },
    "flatline": {
        "desc": FRONTEND.WPN_FLATLINE_DESC,
        "longdesc": FRONTEND.WPN_FLATLINE_LONGDESC,
        "name": FRONTEND.WPN_FLATLINE_NAME,
        "nameshort": FRONTEND.WPN_FLATLINE_NAME_SHORT,
        "class": FRONTEND.WPN_FLATLINE_CLASS,
        "type": FRONTEND.WPN_FLATLINE_TYPE,
    },
    "g2a5": {
        "desc": FRONTEND.WPN_G2A5_DESC,
        "longdesc": FRONTEND.WPN_G2A5_LONGDESC,
        "name": FRONTEND.WPN_G2A5_NAME,
        "nameshort": FRONTEND.WPN_G2A5_NAME_SHORT,
        "class": FRONTEND.WPN_G2A5_CLASS,
        "type": FRONTEND.WPN_G2A5_TYPE,
    },
    "hemlok": {
        "desc": FRONTEND.WPN_HEMLOK_DESC,
        "longdesc": FRONTEND.WPN_HEMLOK_LONGDESC,
        "name": FRONTEND.WPN_HEMLOK_NAME,
        "nameshort": FRONTEND.WPN_HEMLOK_NAME_SHORT,
        "class": FRONTEND.WPN_HEMLOK_CLASS,
        "type": FRONTEND.WPN_HEMLOK_TYPE,
    },
    "kraber": {
        "desc": FRONTEND.WPN_KRABER_DESC,
        "longdesc": FRONTEND.WPN_KRABER_LONGDESC,
        "name": FRONTEND.WPN_KRABER_NAME,
        "nameshort": FRONTEND.WPN_KRABER_NAME_SHORT,
        "class": FRONTEND.WPN_KRABER_CLASS,
        "type": FRONTEND.WPN_KRABER_TYPE,
    },
    "leadwall": {
        "desc": FRONTEND.WPN_LEADWALL_DESC,
        "longdesc": FRONTEND.WPN_LEADWALL_LONGDESC,
        "name": FRONTEND.WPN_LEADWALL_NAME,
        "nameshort": FRONTEND.WPN_LEADWALL_NAME_SHORT,
        "class": FRONTEND.WPN_LEADWALL_CLASS,
        "type": FRONTEND.WPN_LEADWALL_TYPE,
    },
    "longbow": {
        "desc": FRONTEND.WPN_LONGBOW_DESC,
        "longdesc": FRONTEND.WPN_LONGBOW_LONGDESC,
        "name": FRONTEND.WPN_LONGBOW_NAME,
        "nameshort": FRONTEND.WPN_LONGBOW_NAME_SHORT,
        "class": FRONTEND.WPN_LONGBOW_CLASS,
        "type": FRONTEND.WPN_LONGBOW_TYPE,
    },
    "lstar": {
        "desc": FRONTEND.WPN_LSTAR_DESC,
        "longdesc": FRONTEND.WPN_LSTAR_LONGDESC,
        "name": FRONTEND.WPN_LSTAR_NAME,
        "nameshort": FRONTEND.WPN_LSTAR_NAME_SHORT,
        "class": FRONTEND.WPN_LSTAR_CLASS,
        "type": FRONTEND.WPN_LSTAR_TYPE,
    },
    "mastiff": {
        "desc": FRONTEND.WPN_MASTIFF_DESC,
        "longdesc": FRONTEND.WPN_MASTIFF_LONGDESC,
        "name": FRONTEND.WPN_MASTIFF_NAME,
        "nameshort": FRONTEND.WPN_MASTIFF_NAME_SHORT,
        "class": FRONTEND.WPN_MASTIFF_CLASS,
        "type": FRONTEND.WPN_MASTIFF_TYPE,
    },
    "mgl": {
        "desc": FRONTEND.WPN_MGL_DESC,
        "longdesc": FRONTEND.WPN_MGL_LONGDESC,
        "name": FRONTEND.WPN_MGL_NAME,
        "nameshort": FRONTEND.WPN_MGL_NAME_SHORT,
        "class": FRONTEND.WPN_MGL_CLASS,
        "type": FRONTEND.WPN_MGL_TYPE,
    },
    "mozambique": {
        "desc": FRONTEND.WPN_MOZAMBIQUE_DESC,
        "longdesc": FRONTEND.WPN_MOZAMBIQUE_LONGDESC,
        "name": FRONTEND.WPN_MOZAMBIQUE_NAME,
        "nameshort": FRONTEND.WPN_MOZAMBIQUE_NAME_SHORT,
        "class": FRONTEND.WPN_MOZAMBIQUE_CLASS,
        "type": FRONTEND.WPN_MOZAMBIQUE_TYPE,
    },
    "p2016": {
        "desc": FRONTEND.WPN_P2016_DESC,
        "longdesc": FRONTEND.WPN_P2016_LONGDESC,
        "name": FRONTEND.WPN_P2016_NAME,
        "nameshort": FRONTEND.WPN_P2016_NAME_SHORT,
        "class": FRONTEND.WPN_P2016_CLASS,
        "type": FRONTEND.WPN_P2016_TYPE,
    },
    "splitter": {
        "desc": FRONTEND.WPN_SPLITTER_DESC,
        "longdesc": FRONTEND.WPN_SPLITTER_LONGDESC,
        "name": FRONTEND.WPN_SPLITTER_NAME,
        "nameshort": FRONTEND.WPN_SPLITTER_NAME_SHORT,
        "class": FRONTEND.WPN_SPLITTER_CLASS,
        "type": FRONTEND.WPN_SPLITTER_TYPE,
    },
    "predator": {
        "desc": FRONTEND.WPN_PREDATOR_DESC,
        "longdesc": FRONTEND.WPN_PREDATOR_LONGDESC,
        "name": FRONTEND.WPN_PREDATOR_NAME,
        "nameshort": FRONTEND.WPN_PREDATOR_NAME_SHORT,
        "class": FRONTEND.WPN_PREDATOR_CLASS,
        "type": FRONTEND.WPN_PREDATOR_TYPE,
    },
    "r101": {
        "desc": FRONTEND.WPN_R101_DESC,
        "longdesc": FRONTEND.WPN_R101_LONGDESC,
        "name": FRONTEND.WPN_R101_NAME,
        "nameshort": FRONTEND.WPN_R101_NAME_SHORT,
        "class": FRONTEND.WPN_R101_CLASS,
        "type": FRONTEND.WPN_R101_TYPE,
    },
    "r201": {
        "desc": FRONTEND.WPN_R201_DESC,
        "longdesc": FRONTEND.WPN_R201_LONGDESC,
        "name": FRONTEND.WPN_R201_NAME,
        "nameshort": FRONTEND.WPN_R201_NAME_SHORT,
        "class": FRONTEND.WPN_R201_CLASS,
        "type": FRONTEND.WPN_R201_TYPE,
    },
    "r97": {
        "desc": FRONTEND.WPN_R97_DESC,
        "longdesc": FRONTEND.WPN_R97_LONGDESC,
        "name": FRONTEND.WPN_R97_NAME,
        "nameshort": FRONTEND.WPN_R97_NAME_SHORT,
        "class": FRONTEND.WPN_R97_CLASS,
        "type": FRONTEND.WPN_R97_TYPE,
    },
    "railgun": {
        "desc": FRONTEND.WPN_RAILGUN_DESC,
        "longdesc": FRONTEND.WPN_RAILGUN_LONGDESC,
        "name": FRONTEND.WPN_RAILGUN_NAME,
        "nameshort": FRONTEND.WPN_RAILGUN_NAME_SHORT,
        "class": FRONTEND.WPN_RAILGUN_CLASS,
        "type": FRONTEND.WPN_RAILGUN_TYPE,
    },
    "re45": {
        "desc": FRONTEND.WPN_RE45_DESC,
        "longdesc": FRONTEND.WPN_RE45_LONGDESC,
        "name": FRONTEND.WPN_RE45_NAME,
        "nameshort": FRONTEND.WPN_RE45_NAME_SHORT,
        "class": FRONTEND.WPN_RE45_CLASS,
        "type": FRONTEND.WPN_RE45_TYPE,
    },
    "mk6": {
        "desc": FRONTEND.WPN_MK6_DESC,
        "longdesc": FRONTEND.WPN_MK6_LONGDESC,
        "name": FRONTEND.WPN_MK6_NAME,
        "nameshort": FRONTEND.WPN_MK6_NAME_SHORT,
        "class": FRONTEND.WPN_MK6_CLASS,
        "type": FRONTEND.WPN_MK6_TYPE,
    },
    "smr": {
        "desc": FRONTEND.WPN_SMR_DESC,
        "longdesc": FRONTEND.WPN_SMR_LONGDESC,
        "name": FRONTEND.WPN_SMR_NAME,
        "nameshort": FRONTEND.WPN_SMR_NAME_SHORT,
        "class": FRONTEND.WPN_SMR_CLASS,
        "type": FRONTEND.WPN_SMR_TYPE,
    },
    "softball": {
        "desc": FRONTEND.WPN_SOFTBALL_DESC,
        "longdesc": FRONTEND.WPN_SOFTBALL_LONGDESC,
        "name": FRONTEND.WPN_SOFTBALL_NAME,
        "nameshort": FRONTEND.WPN_SOFTBALL_NAME_SHORT,
        "class": FRONTEND.WPN_SOFTBALL_CLASS,
        "type": FRONTEND.WPN_SOFTBALL_TYPE,
    },
    "spitfire": {
        "desc": FRONTEND.WPN_SPITFIRE_DESC,
        "longdesc": FRONTEND.WPN_SPITFIRE_LONGDESC,
        "name": FRONTEND.WPN_SPITFIRE_NAME,
        "nameshort": FRONTEND.WPN_SPITFIRE_NAME_SHORT,
        "class": FRONTEND.WPN_SPITFIRE_CLASS,
        "type": FRONTEND.WPN_SPITFIRE_TYPE,
    },
    "t203": {
        "desc": FRONTEND.WPN_T203_DESC,
        "longdesc": FRONTEND.WPN_T203_LONGDESC,
        "name": FRONTEND.WPN_T203_NAME,
        "nameshort": FRONTEND.WPN_T203_NAME_SHORT,
        "class": FRONTEND.WPN_T203_CLASS,
        "type": FRONTEND.WPN_T203_TYPE,
    },
    "thr40mm": {
        "desc": FRONTEND.WPN_THR40MM_DESC,
        "longdesc": FRONTEND.WPN_THR40MM_LONGDESC,
        "name": FRONTEND.WPN_THR40MM_NAME,
        "nameshort": FRONTEND.WPN_THR40MM_NAME_SHORT,
        "class": FRONTEND.WPN_THR40MM_CLASS,
        "type": FRONTEND.WPN_THR40MM_TYPE,
    },
    "thunderbolt": {
        "desc": FRONTEND.WPN_THUNDERBOLT_DESC,
        "longdesc": FRONTEND.WPN_THUNDERBOLT_LONGDESC,
        "name": FRONTEND.WPN_THUNDERBOLT_NAME,
        "nameshort": FRONTEND.WPN_THUNDERBOLT_NAME_SHORT,
        "class": FRONTEND.WPN_THUNDERBOLT_CLASS,
        "type": FRONTEND.WPN_THUNDERBOLT_TYPE,
    },
    "volt": {
        "desc": FRONTEND.WPN_VOLT_DESC,
        "longdesc": FRONTEND.WPN_VOLT_LONGDESC,
        "name": FRONTEND.WPN_VOLT_NAME,
        "nameshort": FRONTEND.WPN_VOLT_NAME_SHORT,
        "class": FRONTEND.WPN_VOLT_CLASS,
        "type": FRONTEND.WPN_VOLT_TYPE,
    },
    "wingman": {
        "desc": FRONTEND.WPN_WINGMAN_DESC,
        "longdesc": FRONTEND.WPN_WINGMAN_LONGDESC,
        "name": FRONTEND.WPN_WINGMAN_NAME,
        "nameshort": FRONTEND.WPN_WINGMAN_NAME_SHORT,
        "class": FRONTEND.WPN_WINGMAN_CLASS,
        "type": FRONTEND.WPN_WINGMAN_TYPE,
    },
    "wingmann": {
        "desc": FRONTEND.WPN_WINGMANN_DESC,
        "longdesc": FRONTEND.WPN_WINGMANN_LONGDESC,
        "name": FRONTEND.WPN_WINGMANN_NAME,
        "nameshort": FRONTEND.WPN_WINGMANN_NAME_SHORT,
        "class": FRONTEND.WPN_WINGMANN_CLASS,
        "type": FRONTEND.WPN_WINGMANN_TYPE,
    },
    "chaingun": {
        "desc": FRONTEND.WPN_CHAINGUN_DESC,
        "longdesc": FRONTEND.WPN_CHAINGUN_LONGDESC,
        "name": FRONTEND.WPN_CHAINGUN_NAME,
        "nameshort": FRONTEND.WPN_CHAINGUN_NAME_SHORT,
        "class": FRONTEND.WPN_CHAINGUN_CLASS,
        "type": FRONTEND.WPN_CHAINGUN_TYPE,
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
