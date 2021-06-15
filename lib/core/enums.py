# LPL - Local Python Libraries
from backend import ROOT_DIR


class DATA(object):  # Data folder
    WEAPON_SKIN = r"{0}\data\materials\weapons".format(ROOT_DIR)
    WEAPON_ICON = r"{0}\data\images\weapon_icons".format(ROOT_DIR)


class NETWORK(object):
    API_LOCAL_PORT = 5883
    API_NOSKILL_PORT = 4242
    SERVER_DOMAIN = ""  # TODO
    SERVER_SUBDOMAIN_API = "api"
    SERVER_SUBDOMAIN_WORKSHOP = "workshop"
    MESSAGE_ERROR = "error"
    MESSAGE_SUCCESS = "success"
    USER_AGENT = "titanfall-2-toolkit"
    URL_API = "http://127.0.0.1:4242"
    # URL_API = "https://{0}.{1}".format(SERVER_SUBDOMAIN_API, SERVER_DOMAIN)  # Don't forget the port at the end
    URL_WORKSHOP = "https://{0}.{1}".format(SERVER_SUBDOMAIN_WORKSHOP, SERVER_DOMAIN)


class TEXTURE(object):
    AMBIENTOCC = "ambiant_occ"
    BASE = "color"
    BASE2 = "color2"
    BLENDMODULATE = "blend"
    BUMP = "normal"
    CORNEA = "cornea"
    DETAIL = "detail"
    ENV = "env"
    ENVMASK = "env_mask"
    PHONGEXPONENT = "phong"
    SELFILLUM = "illum_mask"


class WPN(object):
    CLASS_PILOT_AT = "Pilot Anti-Titan"
    CLASS_PILOT_ORDNANCE = "Pilot Ordnance"
    CLASS_PILOT_PISTOL = "Pilot Pistol"
    CLASS_PILOT_PRIMARY = "Pilot Primary"
    CLASS_TITAN_ORDNANCE = "Titan Ordnance"
    CLASS_TITAN_PRIMARY = "Titan Primary"
    FILE_404 = "File does not exist"
    FILE_PATH_ICON = r"data\images\weapon_icons"
    FILE_TYPE_1P = "1P"  # First person view
    FILE_TYPE_3P = "3P"  # Third person view
    FILE_TYPE_HP = "HP"  # Holster view
    FILE_TYPE_MP = "MP"  # Menus view
    FILE_UNKNOWN = "File is unknown"
    TYPE_AR = "Assault Rifle"
    TYPE_AT = "Anti-Titan"
    TYPE_EXPLOSIVE = "Explosive"
    TYPE_GRENADIER = "Grenadier"
    TYPE_LMG = "Light Machine Gun"
    TYPE_MELEE = "Melee"
    TYPE_PISTOL = "Pistol"
    TYPE_SHOTGUN = "Shotgun"
    TYPE_SMG = "Submachine Gun"
    TYPE_SR = "Sniper Rifle"
    VERSION_1 = "1"
    VERSION_2 = "2"
    VERSION_VANILLA = "vanilla"


class FRONTEND(object):
    # TODO add ordnances
    # TODO add melees
    # TODO add robots (ticks, marvin, specters, etc.)
    # TODO add humans
    WPN_ALTERNATOR_DESC = "Twin Barrel SMG."
    WPN_ALTERNATOR_LONGDESC = "The Alternator (also referred to as the SP-14 Hatchet in concept art) is a Pilot anti-personnel twin-barrel submachine gun manufactured by Emslie Tactical."
    WPN_ALTERNATOR_NAME = "Alternator"
    WPN_ALTERNATOR_NAME_SHORT = "alternator"
    WPN_ALTERNATOR_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_ALTERNATOR_TYPE = WPN.TYPE_SMG

    WPN_ARCHER_DESC = "Rocket Launcher with Anti-Titan lock-on."
    WPN_ARCHER_LONGDESC = "The Archer Heavy Rocket, also known simply as the Archer, is an anti-Titan lock-on rocket launcher manufactured by Brockhaurd Manufacturing."
    WPN_ARCHER_NAME = "Archer"
    WPN_ARCHER_NAME_SHORT = "archer"
    WPN_ARCHER_CLASS = WPN.CLASS_PILOT_AT
    WPN_ARCHER_TYPE = WPN.TYPE_AT

    WPN_CAR_DESC = "Consistent recoil SMG."
    WPN_CAR_LONGDESC = "The Combat Advanced Round Submachine Gun (C.A.R. SMG) is a Pilot anti-personnel fully automatic submachine gun that appears in Titanfall and Titanfall 2"
    WPN_CAR_NAME = "CAR"
    WPN_CAR_NAME_SHORT = "car"
    WPN_CAR_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_CAR_TYPE = WPN.TYPE_SMG

    WPN_COLDWAR_DESC = "4-round burst Grenadier weapon."
    WPN_COLDWAR_LONGDESC = "The EM-4 Cold War is a primary four-round burst bullpup grenade launcher manufactured by Vinson Dynamics, firing 4.73x33mm explosive ammunition."
    WPN_COLDWAR_NAME = "EM-4 Cold War"
    WPN_COLDWAR_NAME_SHORT = "coldwar"
    WPN_COLDWAR_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_COLDWAR_TYPE = WPN.TYPE_GRENADIER

    WPN_DEFENDER_DESC = "Charged precision beam Anti-Titan sniper."
    WPN_DEFENDER_LONGDESC = "The Charge Rifle fires an energy beam that inflicts massive damage. Holding the trigger charges the weapon."
    WPN_DEFENDER_NAME = "Charge Rifle"
    WPN_DEFENDER_NAME_SHORT = "defender"
    WPN_DEFENDER_CLASS = WPN.CLASS_PILOT_AT
    WPN_DEFENDER_TYPE = WPN.TYPE_AT

    WPN_DEVOTION_DESC = "Ramps up fire rate over time."
    WPN_DEVOTION_LONGDESC = "The X-55 Devotion is a light machine guns (LMGs). Its fire rate increases greatly the longer the trigger is held."
    WPN_DEVOTION_NAME = "X-55 Devotion"
    WPN_DEVOTION_NAME_SHORT = "devotion"
    WPN_DEVOTION_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_DEVOTION_TYPE = WPN.TYPE_LMG

    WPN_DOUBLETAKE_DESC = "Twin-fire sniper rifle."
    WPN_DOUBLETAKE_LONGDESC = "The D-2 Double Take is a Pilot anti-personnel semi-automatic twin-barrel bullpup marksman rifle manufactured by Burrell Defense"
    WPN_DOUBLETAKE_NAME = "D-2 Double Take"
    WPN_DOUBLETAKE_NAME_SHORT = "doubletake"
    WPN_DOUBLETAKE_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_DOUBLETAKE_TYPE = WPN.TYPE_SR

    WPN_EPG_DESC = "Single fire, direct energy propelled launcher."
    WPN_EPG_LONGDESC = "The EPG-1, or Energy Propelled Grenade, is an advanced plasma antipersonnel grenade launcher appearing in Titanfall 2. It fires slow-moving blue plasma grenades with high splash damage."
    WPN_EPG_NAME = "EPG-1"
    WPN_EPG_NAME_SHORT = "epg"
    WPN_EPG_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_EPG_TYPE = WPN.TYPE_GRENADIER

    WPN_EVA8_DESC = "Fully automatic shotgun."
    WPN_EVA8_LONGDESC = "The EVA-8 (Extra-Vehicular Activity) Automatic Shotgun is a Pilot anti-personnel auto-loading shotgun manufactured by Wonyeon Defense."
    WPN_EVA8_NAME = "EVA-8 Auto"
    WPN_EVA8_NAME_SHORT = "eva8"
    WPN_EVA8_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_EVA8_TYPE = WPN.TYPE_SHOTGUN

    WPN_FLATLINE_DESC = "Full-auto with a punch."
    WPN_FLATLINE_LONGDESC = "The V-47 Flatline is a Pilot anti-personnel fully automatic bullpup assault rifle, manufactured by Wonyeon Defense. It has negligible vertical recoil, instead involving an extreme degree of horizontal recoil, similar to the Alternator."
    WPN_FLATLINE_NAME = "V-47 Flatline"
    WPN_FLATLINE_NAME_SHORT = "flatline"
    WPN_FLATLINE_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_FLATLINE_TYPE = WPN.TYPE_AR

    WPN_G2A5_DESC = "Semi-auto precision rifle."
    WPN_G2A5_LONGDESC = "The G2A5 is a semiautomatic battle rifle manufactured by Lastimosa Armory and the successor to the G2A4 Battle Rifle. It is a Pilot primary weapon with perfect accuracy."
    WPN_G2A5_NAME = "G2A5"
    WPN_G2A5_NAME_SHORT = "g2a5"
    WPN_G2A5_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_G2A5_TYPE = WPN.TYPE_AR

    WPN_HEMLOK_DESC = "Burst-fire assault rifle."
    WPN_HEMLOK_LONGDESC = "The M1A3 Hemlok BF-R (Burst-Fire Rifle) is a Pilot anti-personnel burst fire assault rifle."
    WPN_HEMLOK_NAME = "Hemlok BF-R"
    WPN_HEMLOK_NAME_SHORT = "hemlok"
    WPN_HEMLOK_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_HEMLOK_TYPE = WPN.TYPE_AR

    WPN_KRABER_DESC = "Scoped heavy rifle."
    WPN_KRABER_LONGDESC = "The Kraber-AP (Armor Penetrating) 14.5x114mm Sniper Rifle is a Pilot anti-personnel bolt-action heavy sniper rifle. It is manufactured by Lastimosa Armory."
    WPN_KRABER_NAME = "Kraber-AP Sniper"
    WPN_KRABER_NAME_SHORT = "kraber"
    WPN_KRABER_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_KRABER_TYPE = WPN.TYPE_SR

    WPN_LEADWALL_DESC = "Projectile shotgun with a wide spread."
    WPN_LEADWALL_LONGDESC = "The Leadwall is the primary Titan weapon for Ronin in Titanfall 2. It is a shotgun, based on the same design as the Triple Threat grenade launcher of Titanfall."
    WPN_LEADWALL_NAME = "Leadwall"
    WPN_LEADWALL_NAME_SHORT = "leadwall"
    WPN_LEADWALL_CLASS = WPN.CLASS_TITAN_PRIMARY
    WPN_LEADWALL_TYPE = WPN.CLASS_TITAN_PRIMARY

    WPN_LONGBOW_DESC = "Semi-auto sniper."
    WPN_LONGBOW_LONGDESC = "The D-101 Longbow-DMR (Designated Marksman Rifle) Sniper Rifle is a Pilot anti-personnel semi-automatic sniper rifle manufactured by Lastimosa Armory. The DMR is a variant of the R-101 Assault Rifle, modified into a marksman rifle role."
    WPN_LONGBOW_NAME = "Longbow-DMR"
    WPN_LONGBOW_NAME_SHORT = "longbow"
    WPN_LONGBOW_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_LONGBOW_TYPE = WPN.TYPE_SR

    WPN_LSTAR_DESC = "Rapid fire energy LMG."
    WPN_LSTAR_LONGDESC = "The L-STAR (Lastimosa Armory Assault Rifle) is a Pilot anti-personnel fully automatic particle accelerating light machine gun manufactured by Lastimosa Armory."
    WPN_LSTAR_NAME = "L-STAR"
    WPN_LSTAR_NAME_SHORT = "lstar"
    WPN_LSTAR_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_LSTAR_TYPE = WPN.TYPE_LMG

    WPN_MASTIFF_DESC = "Auto-loading shotgun with wide spread."
    WPN_MASTIFF_LONGDESC = "The M1901 Mastiff Combat Shotgun is a Pilot anti-personnel energy semi-automatic shotgun manufactured by Lastimosa Armory."
    WPN_MASTIFF_NAME = "Mastiff"
    WPN_MASTIFF_NAME_SHORT = "mastiff"
    WPN_MASTIFF_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_MASTIFF_TYPE = WPN.TYPE_SHOTGUN

    WPN_MGL_DESC = "Magnetic grenade launcher."
    WPN_MGL_LONGDESC = "The MGL , also known as the Mag Launcher or Magnetic Grenade Launcher, is a Pilot anti-Titan magnetic grenade launcher manufactured by Wonyeon Defense."
    WPN_MGL_NAME = "MGL Mag Launcher"
    WPN_MGL_NAME_SHORT = "mgl"
    WPN_MGL_CLASS = WPN.CLASS_PILOT_AT
    WPN_MGL_TYPE = WPN.TYPE_GRENADIER

    WPN_MOZAMBIQUE_DESC = "Controlled spread triple barrel shotgun pistol."
    WPN_MOZAMBIQUE_LONGDESC = "The SA-3 Mozambique, also knowns as the Mozambique Shotgun is a Pilot anti-personnel, triple-barreled shotgun pistol."
    WPN_MOZAMBIQUE_NAME = "SA-3 Mozambique"
    WPN_MOZAMBIQUE_NAME_SHORT = "mozambique"
    WPN_MOZAMBIQUE_CLASS = WPN.CLASS_PILOT_PISTOL
    WPN_MOZAMBIQUE_TYPE = WPN.TYPE_PISTOL

    WPN_P2016_DESC = "Precision semi-auto pistol."
    WPN_P2016_LONGDESC = "The Hammond P2016 is a sidearm manufactured by Lastimosa Armory. Like its predecessor, the P2016 is a Semi-Automatic Handgun."
    WPN_P2016_NAME = "Hammond P2016"
    WPN_P2016_NAME_SHORT = "p2016"
    WPN_P2016_CLASS = WPN.CLASS_PILOT_PISTOL
    WPN_P2016_TYPE = WPN.TYPE_PISTOL

    WPN_SPLITTER_DESC = "Drains energy to split the shot, increasing damage"
    WPN_SPLITTER_LONGDESC = "The Splitter Rifle (Otherwise known as the Titan Particle Accelerator or TPAR)is a Titan fully-automatic energy rifle"
    WPN_SPLITTER_NAME = "Splitter Rifle"
    WPN_SPLITTER_NAME_SHORT = "splitter"
    WPN_SPLITTER_CLASS = WPN.CLASS_TITAN_PRIMARY
    WPN_SPLITTER_TYPE = WPN.CLASS_TITAN_PRIMARY

    WPN_PREDATOR_DESC = "Heavy minigun"
    WPN_PREDATOR_LONGDESC = "Powerful minigun with a long spin-up time."
    WPN_PREDATOR_NAME = "Predator Cannon"
    WPN_PREDATOR_NAME_SHORT = "predator"
    WPN_PREDATOR_CLASS = WPN.CLASS_TITAN_PRIMARY
    WPN_PREDATOR_TYPE = WPN.CLASS_TITAN_PRIMARY

    WPN_R101_DESC = "Factory issue scoped predecessor of the R-201 rifle."
    WPN_R101_LONGDESC = "The R-101C (Compact) Carbine is a Pilot anti-personnel fully automatic carbine manufactured by Lastimosa Armory."
    WPN_R101_NAME = "R-101 Carbine"
    WPN_R101_NAME_SHORT = "r101"
    WPN_R101_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_R101_TYPE = WPN.TYPE_AR

    WPN_R201_DESC = "Full-auto and high accuracy."
    WPN_R201_LONGDESC = "The R-201 Special Operations Assault Rifle (SOAR) is a Pilot anti-personnel fully automatic assault rifle manufactured by Lastimosa Armory, serving as the successor to the R-101C Carbine and the predecessor to the R-301 Carbine."
    WPN_R201_NAME = "R-201 Carbine"
    WPN_R201_NAME_SHORT = "r201"
    WPN_R201_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_R201_TYPE = WPN.TYPE_AR

    WPN_R97_DESC = "Rapid fire SMG."
    WPN_R97_LONGDESC = "The R-97 Compact Submachine Gun (SMG) is a Pilot anti-personnel close-quarter submachine gun manufactured by Lastimosa Armory."
    WPN_R97_NAME = "R-97"
    WPN_R97_NAME_SHORT = "r97"
    WPN_R97_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_R97_TYPE = WPN.TYPE_SMG

    WPN_RAILGUN_DESC = "Charges up while zoomed."
    WPN_RAILGUN_LONGDESC = "Sniper railgun that charges up while zoomed."
    WPN_RAILGUN_NAME = "Plasma Railgun"
    WPN_RAILGUN_NAME_SHORT = "railgun"
    WPN_RAILGUN_CLASS = WPN.CLASS_TITAN_PRIMARY
    WPN_RAILGUN_TYPE = WPN.CLASS_TITAN_PRIMARY

    WPN_RE45_DESC = ".45 cal full-auto pistol."
    WPN_RE45_LONGDESC = "The RE-45 Autopistol is a Pilot anti-personnel fully automatic machine pistol, manufactured by Lastimosa Armory and Paradinha Arsenal. It serves as a reliable 'spray-and-pray' backup sidearm for pilots at close range."
    WPN_RE45_NAME = "REEEEEEEE"
    WPN_RE45_NAME_SHORT = "re45"
    WPN_RE45_CLASS = WPN.CLASS_PILOT_PISTOL
    WPN_RE45_TYPE = WPN.TYPE_PISTOL

    WPN_MK6_DESC = "Idiot pistol"
    WPN_MK6_LONGDESC = "The next generation in AI targeting technology comes in the form of the Lastimosa Armory Smart Pistol MK6. Upgrades from the MK5 include a reciprocating charging handle, frame integrated ammo counter, multi-function Laser Aiming Module (LAM), etc."
    WPN_MK6_NAME = "Smart Pistol MK6"
    WPN_MK6_NAME_SHORT = "mk6"
    WPN_MK6_CLASS = WPN.CLASS_PILOT_PISTOL
    WPN_MK6_TYPE = WPN.TYPE_PISTOL

    WPN_SMR_DESC = "Rapidly fires micro-missiles."
    WPN_SMR_LONGDESC = "The Anti-Titan Sidewinder Micro Rocket launcher (AT-SMR), is an Anti-Titan Automatic Rocket Launcher (AT-ARL). It is manufactured by Wonyeon Defense."
    WPN_SMR_NAME = "Sidewinder SMR"
    WPN_SMR_NAME_SHORT = "smr"
    WPN_SMR_CLASS = WPN.CLASS_PILOT_AT
    WPN_SMR_TYPE = WPN.TYPE_AT

    WPN_SOFTBALL_DESC = "Adhesive grenade launcher."
    WPN_SOFTBALL_LONGDESC = "The R-6P Softball Anti-Armor Grenade Launcher (AAGL) is a Pilot anti-Titan/personnel grenade launcher"
    WPN_SOFTBALL_NAME = "R-6P Softball"
    WPN_SOFTBALL_NAME_SHORT = "softball"
    WPN_SOFTBALL_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_SOFTBALL_TYPE = WPN.TYPE_GRENADIER

    WPN_SPITFIRE_DESC = "Steady fire rate with a punch."
    WPN_SPITFIRE_LONGDESC = "The Spitfire Light Machine Gun (LMG) is a Pilot anti-personnel fully automatic light machine gun."
    WPN_SPITFIRE_NAME = "Spitfire"
    WPN_SPITFIRE_NAME_SHORT = "spitfire"
    WPN_SPITFIRE_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_SPITFIRE_TYPE = WPN.TYPE_LMG

    WPN_T203_DESC = "Ignites the impact area."
    WPN_T203_LONGDESC = "Giant thermite grenades ignite the impact area."
    WPN_T203_NAME = "T-203 Thermite Launcher"
    WPN_T203_NAME_SHORT = "t203"
    WPN_T203_CLASS = WPN.CLASS_TITAN_PRIMARY
    WPN_T203_TYPE = WPN.CLASS_TITAN_PRIMARY

    WPN_THR40MM_DESC = "Semi-auto 40mm HE rounds."
    WPN_THR40MM_LONGDESC = "The factory issue 40mm Cannon is a semi-automatic weapon that fires a high-explosive round with good accuracy."
    WPN_THR40MM_NAME = "40mm Cannon"
    WPN_THR40MM_NAME_SHORT = "thr40mm"
    WPN_THR40MM_CLASS = WPN.CLASS_TITAN_PRIMARY
    WPN_THR40MM_TYPE = WPN.CLASS_TITAN_PRIMARY

    WPN_THUNDERBOLT_DESC = "Fires a powerful ball of electricity."
    WPN_THUNDERBOLT_LONGDESC = "The LG-97 Thunderbolt is a Pilot anti-Titan energy projector that fires a large, slow-moving ball of electricity that causes damage to any unit within a wide radius around its flight path. Upon striking a target, it explodes in a spherical blast."
    WPN_THUNDERBOLT_NAME = "LG-97 Thunderbolt"
    WPN_THUNDERBOLT_NAME_SHORT = "thunderbolt"
    WPN_THUNDERBOLT_CLASS = WPN.CLASS_PILOT_AT
    WPN_THUNDERBOLT_TYPE = WPN.TYPE_AT

    WPN_VOLT_DESC = "Energy actuated SMG."
    WPN_VOLT_LONGDESC = "The Volt is a Pilot energy submachine gun. It is a weapon that fires concentrated bolts of high energy, which are referred to as 'blue tracers'."
    WPN_VOLT_NAME = "Volt"
    WPN_VOLT_NAME_SHORT = "volt"
    WPN_VOLT_CLASS = WPN.CLASS_PILOT_PRIMARY
    WPN_VOLT_TYPE = WPN.TYPE_SMG

    WPN_WINGMAN_DESC = "High-powered revolver."
    WPN_WINGMAN_LONGDESC = "The B3 Wingman is a Pilot anti-personnel revolver handgun sidearm. The Wingman boasts immense high-caliber stopping power and notable accuracy to compensate for its small magazine and relatively slow fire rate."
    WPN_WINGMAN_NAME = "B3 Wingman"
    WPN_WINGMAN_NAME_SHORT = "wingman"
    WPN_WINGMAN_CLASS = WPN.CLASS_PILOT_PISTOL
    WPN_WINGMAN_TYPE = WPN.TYPE_PISTOL

    WPN_WINGMANN_DESC = "Extended range projectile pistol with stock scope."
    WPN_WINGMANN_LONGDESC = "Bish's personal and most trusted sidearm. The B3 Wingman Elite has been customized to fit the needs of an inter-colonial arms dealer with a shady past and even cloudier business practices."
    WPN_WINGMANN_NAME = "Wingman Elite"
    WPN_WINGMANN_NAME_SHORT = "wingmann"
    WPN_WINGMANN_CLASS = WPN.CLASS_PILOT_PISTOL
    WPN_WINGMANN_TYPE = WPN.TYPE_PISTOL

    WPN_CHAINGUN_DESC = "20mm automatic rifle."
    WPN_CHAINGUN_LONGDESC = "20mm automatic rifle."
    WPN_CHAINGUN_NAME = "XO-16"
    WPN_CHAINGUN_NAME_SHORT = "chaingun"
    WPN_CHAINGUN_CLASS = WPN.CLASS_TITAN_PRIMARY
    WPN_CHAINGUN_TYPE = WPN.CLASS_TITAN_PRIMARY
