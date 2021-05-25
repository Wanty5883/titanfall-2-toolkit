# LPL - Local Python Libraries
from lib.core.enums import FRONTEND


"""
█████████████████████████████████████████████████████╗
██                                                 ██║
██      ██████╗ ██╗██╗      ██████╗ ████████╗      ██║
██      ██╔══██╗██║██║     ██╔═══██╗╚══██╔══╝      ██║
██      ██████╔╝██║██║     ██║   ██║   ██║         ██║
██      ██╔═══╝ ██║██║     ██║   ██║   ██║         ██║
██      ██║     ██║███████╗╚██████╔╝   ██║         ██║
██      ╚═╝     ╚═╝╚══════╝ ╚═════╝    ╚═╝         ██║
██                                                 ██║
█████████████████████████████████████████████████████║
╚════════════════════════════════════════════════════╝
"""
"""
                    $$\
                    \__|
 $$$$$$\   $$$$$$\  $$\ $$$$$$\$$$$\   $$$$$$\   $$$$$$\  $$\   $$\
$$  __$$\ $$  __$$\ $$ |$$  _$$  _$$\  \____$$\ $$  __$$\ $$ |  $$ |
$$ /  $$ |$$ |  \__|$$ |$$ / $$ / $$ | $$$$$$$ |$$ |  \__|$$ |  $$ |
$$ |  $$ |$$ |      $$ |$$ | $$ | $$ |$$  __$$ |$$ |      $$ |  $$ |
$$$$$$$  |$$ |      $$ |$$ | $$ | $$ |\$$$$$$$ |$$ |      \$$$$$$$ |
$$  ____/ \__|      \__|\__| \__| \__| \_______|\__|       \____$$ |
$$ |                                                      $$\   $$ |
$$ |                                                      \$$$$$$  |
\__|                                                       \______/
"""


class ALTERNATOR(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\alternator_lmg"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\alternator_smg"
    MATERIAL_1P_NAME_MODDED = "alternator_lmg"
    MATERIAL_1P_NAME_VANILLA = "alternator_smg"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_alternator_smg.mdl"
    MDL_1P_FOLDER = r"models\weapons\alternator_smg"
    MDL_1P_V1_BIN = [(627836, b"\x6c"), (627851, b"\x6c")]
    MDL_1P_V1_BIN_VANILLA = [(627836, b"\x73"), (627851, b"\x73")]
    MDL_1P_V1_HASH = "d472844ee12583c26d98a9018f466213"
    MDL_1P_VANILLA_HASH = "e43a2964ec53f2012f388cb562f65d5b"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_3P_FILE = "w_alternator_smg.mdl"
    # HP - Holster view
    MDL_HP_FILE = "w_alternator_smg_stow.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_ALTERNATOR_DESC
    WPN_LONGDESC = FRONTEND.WPN_ALTERNATOR_LONGDESC
    WPN_NAME = FRONTEND.WPN_ALTERNATOR_NAME


class CAR101(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\car_lmg"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\car_smg"
    MATERIAL_1P_NAME_MODDED = "car_lmg"
    MATERIAL_1P_NAME_VANILLA = "CAR_smg"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_car101.mdl"
    MDL_1P_FOLDER = r"models\weapons\car101"
    MDL_1P_V1_BIN = [(608664, b"\x6c"), (608668, b"\x63\x61\x72\x5f\x6c\x6d\x67")]
    MDL_1P_V1_BIN_VANILLA = [(608664, b"\x73"), (608668, b"\x43\x41\x52\x5f\x73\x6d\x67")]
    MDL_1P_V1_HASH = "ae94670fbad0a05c478fdf2343ad771d"
    MDL_1P_VANILLA_HASH = "ffafbc744228083728f29200dd426eb0"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_car101.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_CAR101_DESC
    WPN_LONGDESC = FRONTEND.WPN_CAR101_LONGDESC
    WPN_NAME = FRONTEND.WPN_CAR101_NAME


class COLDWAR(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\cold4_war"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\pulse_lmg"
    MATERIAL_1P_NAME_MODDED = "cold4_war"
    MATERIAL_1P_NAME_VANILLA = "pulse_lmg"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_pulse_lmg.mdl"
    MDL_1P_FOLDER = r"models\weapons\pulse_lmg"
    MDL_1P_V1_BIN = [
        (687508, b"\x63\x6f\x6c\x64\x34\x5f\x77\x61\x72"),
        (687518, b"\x63\x6f\x6c\x64\x34\x5f\x77\x61\x72")
    ]
    MDL_1P_V1_BIN_VANILLA = [
        (687508, b"\x70\x75\x6c\x73\x65\x5f\x6c\x6d\x67"),
        (687518, b"\x70\x75\x6c\x73\x65\x5f\x6c\x6d\x67")
    ]
    MDL_1P_V1_HASH = "f37d7080bcd98aa7266c665613fb6f80"
    MDL_1P_VANILLA_HASH = "89402845be26fae9bc50830f59b09d82"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_pulse_lmg.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_COLDWAR_DESC
    WPN_LONGDESC = FRONTEND.WPN_COLDWAR_LONGDESC
    WPN_NAME = FRONTEND.WPN_COLDWAR_NAME


class DEVOTION(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\weapons\devotion_"
    MATERIAL_1P_FOLDER_VANILLA = r"models\weapons\hemlok_br"
    MATERIAL_1P_NAME_MODDED = "devotion_"
    MATERIAL_1P_NAME_VANILLA = "hemlok_br"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_hemlock_br.mdl"
    MDL_1P_FOLDER = r"models\weapons\hemlock_br"
    MDL_1P_V1_BIN = [
        (757105, b"\x64\x65\x76\x6f\x74\x69\x6f\x6e\x5f"),
        (757115, b"\x64\x65\x76\x6f\x74\x69\x6f\x6e\x5f")
    ]
    MDL_1P_V1_BIN_VANILLA = [
        (757105, b"\x68\x65\x6d\x6c\x6f\x6b\x5f\x62\x72"),
        (757115, b"\x68\x65\x6d\x6c\x6f\x6b\x5f\x62\x72")
    ]
    MDL_1P_V1_HASH = "2e7825b8f4d4015f8b3c7b684d36395c"
    MDL_1P_VANILLA_HASH = "5aef9f28430a805eb1172115ae4cfc0f"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_hemlock_br.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_DEVOTION_DESC
    WPN_LONGDESC = FRONTEND.WPN_DEVOTION_LONGDESC
    WPN_NAME = FRONTEND.WPN_DEVOTION_NAME


class DOUBLETAKE(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\tripletake_sr"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\doubletake_sr"
    MATERIAL_1P_NAME_MODDED = "tripletake"
    MATERIAL_1P_NAME_VANILLA = "doubletake"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_doubletake.mdl"
    MDL_1P_FOLDER = r"models\weapons\doubletake"
    MDL_1P_V1_BIN = [
        (942419, b"\x74\x72\x69\x70\x6c\x65\x74\x61\x6b\x65\x5f\x73\x72"),
        (942433, b"\x74\x72\x69\x70\x6c\x65\x74\x61\x6b\x65")
    ]
    MDL_1P_V1_BIN_VANILLA = [
        (942419, b"\x64\x6f\x75\x62\x6c\x65\x74\x61\x6b\x65\x5f\x73\x72"),
        (942433, b"\x64\x6f\x75\x62\x6c\x65\x74\x61\x6b\x65")
    ]
    MDL_1P_V1_HASH = "d75873936045bb813039ca86160b0d1b"
    MDL_1P_VANILLA_HASH = "a6cd5d0fab1764cf9158cce06a71f6ff"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_doubletake.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_DOUBLETAKE_DESC
    WPN_LONGDESC = FRONTEND.WPN_DOUBLETAKE_LONGDESC
    WPN_NAME = FRONTEND.WPN_DOUBLETAKE_NAME


class EPG(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\epj"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\epg"
    MATERIAL_1P_NAME_MODDED = "epj"
    MATERIAL_1P_NAME_VANILLA = "epg"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_epg.mdl"
    MDL_1P_FOLDER = r"models\weapons\epg"
    MDL_1P_V1_BIN = [(610289, b"\x65\x70\x6a"), (610293, b"\x65\x70\x6a")]
    MDL_1P_V1_BIN_VANILLA = [(610289, b"\x65\x70\x67"), (610293, b"\x65\x70\x67")]
    MDL_1P_V1_HASH = "22c2c99fb5a846dfc7e2f1d039438b46"
    MDL_1P_VANILLA_HASH = "a94e174bdb8dfea78b779dae66ef3cdf"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_epg.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_EPG_DESC
    WPN_LONGDESC = FRONTEND.WPN_EPG_LONGDESC
    WPN_NAME = FRONTEND.WPN_EPG_NAME


class EVA8(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\eva7_stgn"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\eva8_stgn"
    MATERIAL_1P_NAME_MODDED = "eva7_stgn"
    MATERIAL_1P_NAME_VANILLA = "eva8_stgn"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_w1128.mdl"
    MDL_1P_FOLDER = r"models\weapons\w1128"
    MDL_1P_V1_BIN = [(563204, b"\x37"), (563214, b"\x37")]
    MDL_1P_V1_BIN_VANILLA = [(563204, b"\x38"), (563214, b"\x38")]
    MDL_1P_V1_HASH = "1425b759dfd05dc59cdf804d74d57f67"
    MDL_1P_VANILLA_HASH = "f09961f7d9bb15b12ac3aed23b8b5aac"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_w1128.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_EVA8_DESC
    WPN_LONGDESC = FRONTEND.WPN_EVA8_LONGDESC
    WPN_NAME = FRONTEND.WPN_EVA8_NAME


class FLATLINE(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\weapons\vinson"
    MATERIAL_1P_FOLDER_VANILLA = r"models\weapons\vinson"
    MATERIAL_1P_NAME_MODDED = "flatline_arf"
    MATERIAL_1P_NAME_VANILLA = "vinson_rifle"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_vinson.mdl"
    MDL_1P_FOLDER = r"models\weapons\vinson"
    MDL_1P_V1_BIN = [(639230, b"\x66\x6c\x61\x74\x6c\x69\x6e\x65\x5f\x61\x72\x66")]
    MDL_1P_V1_BIN_VANILLA = [(639230, b"\x76\x69\x6e\x73\x6f\x6e\x5f\x72\x69\x66\x6c\x65")]
    MDL_1P_V1_HASH = "d45a13b7b66eaa4e59a99d34fc8f2829"
    MDL_1P_VANILLA_HASH = "d85f1d546dec75fad24e884bd6ab2101"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_vinson.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_FLATLINE_DESC
    WPN_LONGDESC = FRONTEND.WPN_FLATLINE_LONGDESC
    WPN_NAME = FRONTEND.WPN_FLATLINE_NAME


class G2A5(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\g2a5_ar"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\g2a4_ar"
    MATERIAL_1P_NAME_MODDED = "g2a5_ar"
    MATERIAL_1P_NAME_VANILLA = "g2a4_ar"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_g2a4.mdl"
    MDL_1P_FOLDER = r"models\weapons\g2"
    MDL_1P_V1_BIN = [(616532, b"\x35"), (616540, b"\x35")]
    MDL_1P_V1_BIN_VANILLA = [(616532, b"\x34"), (616540, b"\x34")]
    MDL_1P_V1_HASH = "ede7dad905e40d2b3aa4982562e1180f"
    MDL_1P_VANILLA_HASH = "c47c07d1646a6f7921f34e1d38ebbe69"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_g2a4.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_G2A5_DESC
    WPN_LONGDESC = FRONTEND.WPN_G2A5_LONGDESC
    WPN_NAME = FRONTEND.WPN_G2A5_NAME


class HEMLOK(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\hemlok_cfr_ar"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\hemlok_bfr_ar"
    MATERIAL_1P_NAME_MODDED = "hemlok_cfr_ar"
    MATERIAL_1P_NAME_VANILLA = "hemlok_BFR_ar"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_hemlok.mdl"
    MDL_1P_FOLDER = r"models\weapons\m1a1_hemlok"
    MDL_1P_V1_BIN = [(646701, b"\x63"), (646715, b"\x63\x66\x72")]
    MDL_1P_V1_BIN_VANILLA = [(646701, b"\x62"), (646715, b"\x42\x46\x52")]
    MDL_1P_V1_HASH = "3d72fde9b8db290ffc22b9a264d946cf"
    MDL_1P_VANILLA_HASH = "d2a1e67c84860bfc312b03c19f26d814"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_hemlok.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_HEMLOK_DESC
    WPN_LONGDESC = FRONTEND.WPN_HEMLOK_LONGDESC
    WPN_NAME = FRONTEND.WPN_HEMLOK_NAME


class KRABER(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\kraber_tr"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\kraber_sr"
    MATERIAL_1P_NAME_MODDED = "kraber_tr"
    MATERIAL_1P_NAME_VANILLA = "kraber_sr"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_at_rifle.mdl"
    MDL_1P_FOLDER = r"models\weapons\at_rifle"
    MDL_1P_V1_BIN = [(861702, b"\x74"), (861712, b"\x74")]
    MDL_1P_V1_BIN_VANILLA = [(861702, b"\x73"), (861712, b"\x73")]
    MDL_1P_V1_HASH = "237e66e221119e3cc07a6ab2647a3468"
    MDL_1P_VANILLA_HASH = "a59db6a8942348dadab434a5eb22c818"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_at_rifle.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_KRABER_DESC
    WPN_LONGDESC = FRONTEND.WPN_KRABER_LONGDESC
    WPN_NAME = FRONTEND.WPN_KRABER_NAME


class LONGBOW(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\longbow_cmr"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\Longbow_dmr"
    MATERIAL_1P_NAME_MODDED = "longbow_cmr"
    MATERIAL_1P_NAME_VANILLA = "longbow_dmr"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_rspn101_dmr.mdl"
    MDL_1P_FOLDER = r"models\weapons\rspn101_dmr"
    MDL_1P_V1_BIN = [(624410, b"\x6c"), (624418, b"\x63"), (624430, b"\x63")]
    MDL_1P_V1_BIN_VANILLA = [(624410, b"\x4c"), (624418, b"\x64"), (624430, b"\x64")]
    MDL_1P_V1_HASH = "133a4cd435329a4f6e80f297c802bd15"
    MDL_1P_VANILLA_HASH = "b1dce9fefe55ba03a779bca98c21ea18"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_rspn101_dmr.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_LONGBOW_DESC
    WPN_LONGDESC = FRONTEND.WPN_LONGBOW_LONGDESC
    WPN_NAME = FRONTEND.WPN_LONGBOW_NAME


class LSTAR(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\weapons\lstas"
    MATERIAL_1P_FOLDER_VANILLA = r"models\weapons\lstar"
    MATERIAL_1P_NAME_MODDED = "lstas"
    MATERIAL_1P_NAME_VANILLA = "lstar"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_lstar.mdl"
    MDL_1P_FOLDER = r"models\weapons\lstar"
    MDL_1P_V1_BIN = [(1059670, b"\x73"), (1059676, b"\x73")]
    MDL_1P_V1_BIN_VANILLA = [(1059670, b"\x72"), (1059676, b"\x72")]
    MDL_1P_V1_HASH = "f4b4c270cf8d0849acb053ec379a7a30"
    MDL_1P_VANILLA_HASH = "e774bd7ed35c2fc06a43d61a8d659d1c"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_lstar.mdl"
    # MISC
    MDL_FILE_HP = "w_lstar_stow.mdl"
    MDL_FILE_MP = "ptpov_lstar_menu.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_LSTAR_DESC
    WPN_LONGDESC = FRONTEND.WPN_LSTAR_LONGDESC
    WPN_NAME = FRONTEND.WPN_LSTAR_NAME


class MASTIFF(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\weapons\mastiff_stgo"
    MATERIAL_1P_FOLDER_VANILLA = r"models\weapons\mastiff_stgn"
    MATERIAL_1P_NAME_MODDED = "mastiff_stgo"
    MATERIAL_1P_NAME_VANILLA = "mastiff_stgn"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_mastiff.mdl"
    MDL_1P_FOLDER = r"models\weapons\mastiff_stgn"
    MDL_1P_V1_BIN = [(555217, b"\x6f"), (555230, b"\x6f")]
    MDL_1P_V1_BIN_VANILLA = [(555217, b"\x6e"), (555230, b"\x6e")]
    MDL_1P_V1_HASH = "dd2d31da0d1dad3af7459b7c61812892"
    MDL_1P_VANILLA_HASH = "822241de8ed57fa76fea708937bab58e"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_mastiff.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_MASTIFF_DESC
    WPN_LONGDESC = FRONTEND.WPN_MASTIFF_LONGDESC
    WPN_NAME = FRONTEND.WPN_MASTIFF_NAME


class R101(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\r101_tfp"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\r101_sfp"
    MATERIAL_1P_NAME_MODDED = "r101_tfp"
    MATERIAL_1P_NAME_VANILLA = "r101_sfp"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_r101_sfp.mdl"
    MDL_1P_FOLDER = r"models\weapons\r101_sfp"
    MDL_1P_V1_BIN = [(685216, b"\x74"), (685225, b"\x74")]
    MDL_1P_V1_BIN_VANILLA = [(685216, b"\x73"), (685225, b"\x73")]
    MDL_1P_V1_HASH = "f1a3ac597acce4c222e73fbac8289129"
    MDL_1P_VANILLA_HASH = "d19bfa83ea1703c34309cda246e34194"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_r101_sfp.mdl"
    # MISC
    MDL_FILE_HP = "w_r101_sfp_stow.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_R101_DESC
    WPN_LONGDESC = FRONTEND.WPN_R101_LONGDESC
    WPN_NAME = FRONTEND.WPN_R101_NAME


class R201(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\weapons\r201"
    MATERIAL_1P_FOLDER_VANILLA = r"models\weapons\r101"
    MATERIAL_1P_NAME_MODDED = "r201"
    MATERIAL_1P_NAME_VANILLA = "r101"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_rspn101.mdl"
    MDL_1P_FOLDER = r"models\weapons\rspn101"
    MDL_1P_V1_BIN = [(609696, b"\x32"), (609701, b"\x32")]
    MDL_1P_V1_BIN_VANILLA = [(609696, b"\x31"), (609701, b"\x31")]
    MDL_1P_V1_HASH = "7a965893366faa33f5d833dbf4b3af96"
    MDL_1P_VANILLA_HASH = "02ca186fb737666b78d29b6938c71c40"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_rspn101.mdl"
    # MISC
    MDL_FILE_HP = "w_rspn101_stow.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_R201_DESC
    WPN_LONGDESC = FRONTEND.WPN_R201_LONGDESC
    WPN_NAME = FRONTEND.WPN_R201_NAME


class R97(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\r98"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\r97"
    MATERIAL_1P_NAME_MODDED = "r98_cn"
    MATERIAL_1P_NAME_VANILLA = "R97_CN"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_r97.mdl"
    MDL_1P_FOLDER = r"models\weapons\r97"
    MDL_1P_V1_BIN = [(596425, b"\x38"), (596427, b"\x72\x39\x38\x5f\x63\x6e")]
    MDL_1P_V1_BIN_VANILLA = [(596425, b"\x37"), (596427, b"\x52\x39\x37\x5f\x43\x4e")]
    MDL_1P_V1_HASH = "33a8695df765a26cea87112bf870ea34"
    MDL_1P_VANILLA_HASH = "854d5f860b97bfdd31ba42f2cc5b0de7"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_r97.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_R97_DESC
    WPN_LONGDESC = FRONTEND.WPN_R97_LONGDESC
    WPN_NAME = FRONTEND.WPN_R97_NAME


class SMR(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\sidewinder_mr"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\sidewinder_at"
    MATERIAL_1P_NAME_MODDED = "sidewinder_mr"
    MATERIAL_1P_NAME_VANILLA = "sidewinder_at"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_ARL.mdl"
    MDL_1P_FOLDER = r"models\weapons\auto_rocket_launcher_ARL"
    MDL_1P_V1_BIN = [(869909, b"\x6d\x72"), (869923, b"\x6d\x72")]
    MDL_1P_V1_BIN_VANILLA = [(869909, b"\x61\x74"), (869923, b"\x61\x74")]
    MDL_1P_V1_HASH = "4c62440b097dc4e401db39ccb386e003"
    MDL_1P_VANILLA_HASH = "616ffb2b1e3fc23bc2f1cc69d1932876"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_ARL.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_SMR_DESC
    WPN_LONGDESC = FRONTEND.WPN_SMR_LONGDESC
    WPN_NAME = FRONTEND.WPN_SMR_NAME


class SOFTBALL(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\weapons\softball_mr"
    MATERIAL_1P_FOLDER_VANILLA = r"models\weapons\softball_at"
    MATERIAL_1P_NAME_MODDED = "softball_mr_skin01"
    MATERIAL_1P_NAME_VANILLA = "softball_at_skin01"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_softball_at.mdl"
    MDL_1P_FOLDER = r"models\weapons\softball_at"
    MDL_1P_V1_BIN = [(451899, b"\x6d\x72"), (451911, b"\x6d\x72")]
    MDL_1P_V1_BIN_VANILLA = [(451899, b"\x61\x74"), (451911, b"\x61\x74")]
    MDL_1P_V1_HASH = "b9755febe59e42fe70e1c5fc535d7917"
    MDL_1P_VANILLA_HASH = "7e49257738fc45a257f7b979f8c4a083"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_softball_at.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_SOFTBALL_DESC
    WPN_LONGDESC = FRONTEND.WPN_SOFTBALL_LONGDESC
    WPN_NAME = FRONTEND.WPN_SOFTBALL_NAME


class SPITFIRE(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\spitfire_smg"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\spitfire_lmg"
    MATERIAL_1P_NAME_MODDED = "spitfire_smg"
    MATERIAL_1P_NAME_VANILLA = "spitfire_lmg"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_lmg_hemlok.mdl"
    MDL_1P_FOLDER = r"models\weapons\lmg_hemlok"
    MDL_1P_V1_BIN = [(682288, b"\x73"), (682301, b"\x73")]
    MDL_1P_V1_BIN_VANILLA = [(682288, b"\x6c"), (682301, b"\x6c")]
    MDL_1P_V1_HASH = "5373576625b93574398a8ef12e610ade"
    MDL_1P_VANILLA_HASH = "8eb642219eb5f0c610d16f30dc72ced0"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_lmg_hemlok.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_SPITFIRE_DESC
    WPN_LONGDESC = FRONTEND.WPN_SPITFIRE_LONGDESC
    WPN_NAME = FRONTEND.WPN_SPITFIRE_NAME


class VOLT(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\weapons\voltbrd_smg"
    MATERIAL_1P_FOLDER_VANILLA = r"models\weapons\hemlok_smg"
    MATERIAL_1P_NAME_MODDED = "voltbrd_smg"
    MATERIAL_1P_NAME_VANILLA = "hemlock_smg"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_hemlok_smg.mdl"
    MDL_1P_FOLDER = r"models\weapons\hemlok_smg"
    MDL_1P_V1_BIN = [
        (629644, b"\x76\x6f\x6c\x74\x62\x72\x64"),
        (629655, b"\x76\x6f\x6c\x74\x62\x72\x64"),
    ]
    MDL_1P_V1_BIN_VANILLA = [
        (629644, b"\x68\x65\x6d\x6c\x6f\x63\x6b"),
        (629655, b"\x68\x65\x6d\x6c\x6f\x63\x6b"),
    ]
    MDL_1P_V1_HASH = "db36d9682c1fb4af95cac9284a97a4c6"
    MDL_1P_VANILLA_HASH = "f45f9c9262cc36a70157d4dc8599ba83"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_hemlok_smg.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_VOLT_DESC
    WPN_LONGDESC = FRONTEND.WPN_VOLT_LONGDESC
    WPN_NAME = FRONTEND.WPN_VOLT_NAME


"""
          $$\             $$\               $$\
          \__|            $$ |              $$ |
 $$$$$$\  $$\  $$$$$$$\ $$$$$$\    $$$$$$\  $$ |
$$  __$$\ $$ |$$  _____|\_$$  _|  $$  __$$\ $$ |
$$ /  $$ |$$ |\$$$$$$\    $$ |    $$ /  $$ |$$ |
$$ |  $$ |$$ | \____$$\   $$ |$$\ $$ |  $$ |$$ |
$$$$$$$  |$$ |$$$$$$$  |  \$$$$  |\$$$$$$  |$$ |
$$  ____/ \__|\_______/    \____/  \______/ \__|
$$ |
$$ |
\__|
"""


class MOZAMBIQUE(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\mozambiq"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\pstl_sa3"
    MATERIAL_1P_NAME_MODDED = "mozambiq"
    MATERIAL_1P_NAME_VANILLA = "pstl_sa3"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_pstl_sa3.mdl"
    MDL_1P_FOLDER = r"models\weapons\pstl_sa3"
    MDL_1P_V1_BIN = [
        (579114, b"\x6d\x6f\x7a\x61\x6d\x62\x69\x71"),
        (579123, b"\x6d\x6f\x7a\x61\x6d\x62\x69\x71")
    ]
    MDL_1P_V1_BIN_VANILLA = [
        (579114, b"\x70\x73\x74\x6c\x5f\x73\x61\x33"),
        (579123, b"\x70\x73\x74\x6c\x5f\x73\x61\x33")
    ]
    MDL_1P_V1_HASH = "431afd05d29a9d2e8cf8b013304b7d48"
    MDL_1P_VANILLA_HASH = "8756547f29f3aaa2c4005c1cd374d0f4"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_pstl_sa3.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_MOZAMBIQUE_DESC
    WPN_LONGDESC = FRONTEND.WPN_MOZAMBIQUE_LONGDESC
    WPN_NAME = FRONTEND.WPN_MOZAMBIQUE_NAME


class P2016(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\p2016_pstl"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\p2011_pstl"
    MATERIAL_1P_NAME_MODDED = "p2016_pstl"
    MATERIAL_1P_NAME_VANILLA = "P2011_pstl"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_p2011.mdl"
    MDL_1P_FOLDER = r"models\weapons\p2011"
    MDL_1P_V1_BIN = [(598042, b"\x36"), (598049, b"\x70"), (598053, b"\x36")]
    MDL_1P_V1_BIN_VANILLA = [(598042, b"\x31"), (598049, b"\x50"), (598053, b"\x31")]
    MDL_1P_V1_HASH = "edd97c77a57b0e407adde7cab767e65a"
    MDL_1P_VANILLA_HASH = "2276773f7437bde4fb1e0e5cf14ea4d9"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_p2011.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_P2016_DESC
    WPN_LONGDESC = FRONTEND.WPN_P2016_LONGDESC
    WPN_NAME = FRONTEND.WPN_P2016_NAME


class RE45(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\reeeeeeee"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\re45_pstl"
    MATERIAL_1P_NAME_MODDED = "re45"
    MATERIAL_1P_NAME_VANILLA = "RE45"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_p2011_auto.mdl"
    MDL_1P_FOLDER = r"models\weapons\p2011_auto"
    MDL_1P_V1_BIN = [
        (688694, b"\x72\x65\x65\x65\x65\x65\x65\x65\x65"),
        (688704, b"\x72\x65\x34\x35")
    ]
    MDL_1P_V1_BIN_VANILLA = [
        (688694, b"\x72\x65\x34\x35\x5f\x70\x73\x74\x6c"),
        (688704, b"\x52\x45\x34\x35")
    ]
    MDL_1P_V1_HASH = "a8177fa9741568e6060cd2a4e5de244c"
    MDL_1P_VANILLA_HASH = "3e1e77129d75ac5f74f0bfa30dfcae41"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_p2011_auto.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_RE45_DESC
    WPN_LONGDESC = FRONTEND.WPN_RE45_LONGDESC
    WPN_NAME = FRONTEND.WPN_RE45_NAME


class SMARTPISTOL(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\idiot_pistol"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\smart_pistol"
    MATERIAL_1P_NAME_MODDED = "idiot_pistol_mk7"
    MATERIAL_1P_NAME_VANILLA = "Smart_Pistol_MK6"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_p2011sp.mdl"
    MDL_1P_FOLDER = r"models\weapons\p2011sp"
    MDL_1P_V1_BIN = [
        (564963, b"\x69\x64\x69\x6f\x74"),
        (564976, b"\x69\x64\x69\x6f\x74\x5f\x70\x69\x73\x74\x6f\x6c\x5f\x6d\x6b\x37\x0a")
    ]
    MDL_1P_V1_BIN_VANILLA = [
        (564963, b"\x73\x6d\x61\x72\x74"),
        (564976, b"\x53\x6d\x61\x72\x74\x5f\x50\x69\x73\x74\x6f\x6c\x5f\x4d\x4b\x36\x0a")
    ]
    MDL_1P_V1_HASH = "e8c8a7dc8405548a4d9436570093132e"
    MDL_1P_VANILLA_HASH = "362e8289fee575f4ac5b2c62e84fae6e"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_p2011sp.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_SMARTPISTOL_DESC
    WPN_LONGDESC = FRONTEND.WPN_SMARTPISTOL_LONGDESC
    WPN_NAME = FRONTEND.WPN_SMARTPISTOL_NAME


class WINGMANB3(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\wingman_b3og"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\wingman_pstl"
    MATERIAL_1P_NAME_MODDED = "wingman_b3og"
    MATERIAL_1P_NAME_VANILLA = "wingman_pstl"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_b3wing.mdl"
    MDL_1P_FOLDER = r"models\weapons\b3wing"
    MDL_1P_V1_BIN = [(699297, b"\x62\x33\x6f\x67"), (699310, b"\x62\x33\x6f\x67")]
    MDL_1P_V1_BIN_VANILLA = [(699297, b"\x70\x73\x74\x6c"), (699310, b"\x70\x73\x74\x6c")]
    MDL_1P_V1_HASH = "8c99ce2feee6dd7ba93dc22a04454f31"
    MDL_1P_VANILLA_HASH = "967c4cd2c02e2d0e6fc968a0dd73e170"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_b3wing.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_WINGMANB3_DESC
    WPN_LONGDESC = FRONTEND.WPN_WINGMANB3_LONGDESC
    WPN_NAME = FRONTEND.WPN_WINGMANB3_NAME


class WINGMANN(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\wingman_elpro"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\wingman_elite"
    MATERIAL_1P_NAME_MODDED = "wingman_elpro"
    MATERIAL_1P_NAME_VANILLA = "wingman_elite"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_wingman_elite.mdl"
    MDL_1P_FOLDER = r"models\weapons\wingman_elite"
    MDL_1P_V1_BIN = [
        (681622, b"\x65\x6c\x70\x72\x6f"),
        (681636, b"\x65\x6c\x70\x72\x6f")
    ]
    MDL_1P_V1_BIN_VANILLA = [
        (681622, b"\x65\x6c\x69\x74\x65"),
        (681636, b"\x65\x6c\x69\x74\x65")
    ]
    MDL_1P_V1_HASH = "5ae1e68e104b717e532de579a24351c2"
    MDL_1P_VANILLA_HASH = "92ae5f18b5576a285a1f8b2ad4be283d"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_wingman_elite.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_WINGMANN_DESC
    WPN_LONGDESC = FRONTEND.WPN_WINGMANN_LONGDESC
    WPN_NAME = FRONTEND.WPN_WINGMANN_NAME


"""
                     $$\     $$\          $$\     $$\   $$\
                     $$ |    \__|         $$ |    \__|  $$ |
 $$$$$$\  $$$$$$$\ $$$$$$\   $$\        $$$$$$\   $$\ $$$$$$\    $$$$$$\  $$$$$$$\
 \____$$\ $$  __$$_$$  _|  $$ |$$$$$$_$$  _|  $$ |\_$$  _|   \____$$\ $$  __$$\
 $$$$$$$ |$$ |  $$ | $$ |    $$ |\______| $$ |    $$ |  $$ |     $$$$$$$ |$$ |  $$ |
$$  __$$ |$$ |  $$ | $$ |$$\ $$ |         $$ |$$\ $$ |  $$ |$$\ $$  __$$ |$$ |  $$ |
\$$$$$$$ |$$ |  $$ | \$$$$  |$$ |         \$$$$  |$$ |  \$$$$  |\$$$$$$$ |$$ |  $$ |
 \_______|\__|  \__|  \____/ \__|          \____/ \__|   \____/  \_______|\__|  \__|
"""


class ARCHER(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\archer_sr"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\archer_at"
    MATERIAL_1P_NAME_MODDED = "archer_sr"
    MATERIAL_1P_NAME_VANILLA = "archer_at"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_law.mdl"
    MDL_1P_FOLDER = r"models\weapons\shoulder_rocket_SRAM"
    MDL_1P_V1_BIN = [(667881, b"\x73\x72"), (667891, b"\x73\x72")]
    MDL_1P_V1_BIN_VANILLA = [(667881, b"\x61\x74"), (667891, b"\x61\x74")]
    MDL_1P_V1_HASH = "bec2aa2f24f7e58809645fd07e42a78e"
    MDL_1P_VANILLA_HASH = "1ff33d9dd106cac914dbdee9fee3b1e2"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_shoulder_rocket_SRAM_v2.mdl"
    MDL_FILE_HP = "w_rocket_SRAM_v2_stow.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_ARCHER_DESC
    WPN_LONGDESC = FRONTEND.WPN_ARCHER_LONGDESC
    WPN_NAME = FRONTEND.WPN_ARCHER_NAME


class DEFENDER(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\charge_laser"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\charge_rifle"
    MATERIAL_1P_NAME_MODDED = "charge_laser_sr"
    MATERIAL_1P_NAME_VANILLA = "charge_rifle_at"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_defender.mdl"
    MDL_1P_FOLDER = r"models\weapons\defender"
    MDL_1P_V1_BIN = [
        (486358, b"\x6c\x61\x73\x65\x72"),
        (486371, b"\x6c\x61\x73\x65\x72\x5f\x73\x72")
    ]
    MDL_1P_V1_BIN_VANILLA = [
        (486358, b"\x72\x69\x66\x6c\x65"),
        (486371, b"\x72\x69\x66\x6c\x65\x5f\x61\x74")
    ]
    MDL_1P_V1_HASH = "6b5ef387fc6fb376764ac07f2833a3f1"
    MDL_1P_VANILLA_HASH = "ba5c6f576f75df13af2a57b519657924"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_defender.mdl"
    MDL_FILE_HP = "w_defender_stow.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_DEFENDER_DESC
    WPN_LONGDESC = FRONTEND.WPN_DEFENDER_LONGDESC
    WPN_NAME = FRONTEND.WPN_DEFENDER_NAME


class MGL(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\weapons\mgl_ar"
    MATERIAL_1P_FOLDER_VANILLA = r"models\weapons\mgl_at"
    MATERIAL_1P_NAME_MODDED = "mgl_ar"
    MATERIAL_1P_NAME_VANILLA = "mgl_at"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_mgl_at.mdl"
    MDL_1P_FOLDER = r"models\weapons\mgl_at"
    MDL_1P_V1_BIN = [(1356238, b"\x72"), (1356245, b"\x72")]
    MDL_1P_V1_BIN_VANILLA = [(1356238, b"\x74"), (1356245, b"\x74")]
    MDL_1P_V1_HASH = "2c6de5b83a19915a559497d22a892fbd"
    MDL_1P_VANILLA_HASH = "5ee122587f96931c31f76e51cf6c6aba"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_mgl_at.mdl"
    MDL_FILE_HP = "w_mgl_at_stow.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_MGL_DESC
    WPN_LONGDESC = FRONTEND.WPN_MGL_LONGDESC
    WPN_NAME = FRONTEND.WPN_MGL_NAME


class THUNDERBOLT(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\thunderbolt_"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\arc_launcher"
    MATERIAL_1P_NAME_MODDED = "thunderbolt_"
    MATERIAL_1P_NAME_VANILLA = "arc_launcher"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "ptpov_arc_launcher.mdl"
    MDL_1P_FOLDER = r"models\weapons\arc_launcher"
    MDL_1P_V1_BIN = [
        (519557, b"\x74\x68\x75\x6e\x64\x65\x72\x62\x6f\x6c\x74\x5f"),
        (519570, b"\x74\x68\x75\x6e\x64\x65\x72\x62\x6f\x6c\x74\x5f")
    ]
    MDL_1P_V1_BIN_VANILLA = [
        (519557, b"\x61\x72\x63\x5f\x6c\x61\x75\x6e\x63\x68\x65\x72"),
        (519570, b"\x61\x72\x63\x5f\x6c\x61\x75\x6e\x63\x68\x65\x72")
    ]
    MDL_1P_V1_HASH = "4c4a0813d390c0b3ff0c2af891a9d915"
    MDL_1P_VANILLA_HASH = "c18ad176d9195e49034817b5aa5327d0"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_arc_launcher.mdl"
    MDL_FILE_HP = "w_arc_launcher_stow.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_THUNDERBOLT_DESC
    WPN_LONGDESC = FRONTEND.WPN_THUNDERBOLT_LONGDESC
    WPN_NAME = FRONTEND.WPN_THUNDERBOLT_NAME


"""
███████████████████████████████████████████████████████╗
██                                                   ██║
██      ████████╗██╗████████╗ █████╗ ███╗   ██╗      ██║
██      ╚══██╔══╝██║╚══██╔══╝██╔══██╗████╗  ██║      ██║
██         ██║   ██║   ██║   ███████║██╔██╗ ██║      ██║
██         ██║   ██║   ██║   ██╔══██║██║╚██╗██║      ██║
██         ██║   ██║   ██║   ██║  ██║██║ ╚████║      ██║
██         ╚═╝   ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝      ██║
██                                                   ██║
███████████████████████████████████████████████████████║
╚══════════════════════════════════════════════════════╝
"""
"""
                    $$\
                    \__|
 $$$$$$\   $$$$$$\  $$\ $$$$$$\$$$$\   $$$$$$\   $$$$$$\  $$\   $$\
$$  __$$\ $$  __$$\ $$ |$$  _$$  _$$\  \____$$\ $$  __$$\ $$ |  $$ |
$$ /  $$ |$$ |  \__|$$ |$$ / $$ / $$ | $$$$$$$ |$$ |  \__|$$ |  $$ |
$$ |  $$ |$$ |      $$ |$$ | $$ | $$ |$$  __$$ |$$ |      $$ |  $$ |
$$$$$$$  |$$ |      $$ |$$ | $$ | $$ |\$$$$$$$ |$$ |      \$$$$$$$ |
$$  ____/ \__|      \__|\__| \__| \__| \_______|\__|       \____$$ |
$$ |                                                      $$\   $$ |
$$ |                                                      \$$$$$$  |
\__|                                                       \______/
"""


class LEADWALL(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\titan_leadwall_stgn"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\titan_triple_threat"
    MATERIAL_1P_NAME_MODDED = "leadwall_stgn"
    MATERIAL_1P_NAME_VANILLA = "triple_threat"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "atpov_titan_triple_threat.mdl"
    MDL_1P_FOLDER = r"models\weapons\titan_triple_threat"
    MDL_1P_V1_BIN = [
        (130666, b"\x6c\x65\x61\x64\x77\x61\x6c\x6c\x5f\x73\x74\x67\x6e"),
        (130680, b"\x6c\x65\x61\x64\x77\x61\x6c\x6c\x5f\x73\x74\x67\x6e")
    ]
    MDL_1P_V1_BIN_VANILLA = [
        (130666, b"\x74\x72\x69\x70\x6c\x65\x5f\x74\x68\x72\x65\x61\x74"),
        (130680, b"\x74\x72\x69\x70\x6c\x65\x5f\x74\x68\x72\x65\x61\x74")
    ]
    MDL_1P_V1_HASH = "f5eb2d8c4e0e6eca951271f80c17496e"
    MDL_1P_VANILLA_HASH = "0d3a45aff637d3cc5ac4442162679a01"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_titan_triple_threat.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_LEADWALL_DESC
    WPN_LONGDESC = FRONTEND.WPN_LEADWALL_LONGDESC
    WPN_NAME = FRONTEND.WPN_LEADWALL_NAME


class PARTICLEACCELERATOR(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\weapons\titan_splitter_accelerator"
    MATERIAL_1P_FOLDER_VANILLA = r"models\weapons\titan_particle_accelerator"
    MATERIAL_1P_NAME_MODDED = "titan_splitter_accelerator"
    MATERIAL_1P_NAME_VANILLA = "titan_particle_accelerator"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "atpov_titan_particle_accelerator.mdl"
    MDL_1P_FOLDER = r"models\weapons\titan_particle_accelerator"
    MDL_1P_V1_BIN = [
        (358654, b"\x73\x70\x6c\x69\x74\x74\x65\x72"),
        (358681, b"\x73\x70\x6c\x69\x74\x74\x65\x72")
    ]
    MDL_1P_V1_BIN_VANILLA = [
        (358654, b"\x70\x61\x72\x74\x69\x63\x6c\x65"),
        (358681, b"\x70\x61\x72\x74\x69\x63\x6c\x65")
    ]
    MDL_1P_V1_HASH = "e8b59cd2af6b4cafe76f2f4a0c660fed"
    MDL_1P_VANILLA_HASH = "f945aa95740aac99d108a96a61a53521"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_titan_particle_accelerator.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_PARTICLEACCELERATOR_DESC
    WPN_LONGDESC = FRONTEND.WPN_PARTICLEACCELERATOR_LONGDESC
    WPN_NAME = FRONTEND.WPN_PARTICLEACCELERATOR_NAME


class PREDATORCANNON(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\weapons\predator_gatli"
    MATERIAL_1P_FOLDER_VANILLA = r"models\weapons\predator_titan"
    MATERIAL_1P_NAME_MODDED = "predator_gatli"
    MATERIAL_1P_NAME_VANILLA = "predator_titan"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "atpov_titan_predator.mdl"
    MDL_1P_FOLDER = r"models\weapons\titan_predator"
    MDL_1P_V1_BIN = [
        (376528, b"\x67\x61\x74\x6c\x69"),
        (376543, b"\x67\x61\x74\x6c\x69")
    ]
    MDL_1P_V1_BIN_VANILLA = [
        (376528, b"\x74\x69\x74\x61\x6e"),
        (376543, b"\x74\x69\x74\x61\x6e")
    ]
    MDL_1P_V1_HASH = "ed556151e9d4b9f44337602c4c387925"
    MDL_1P_VANILLA_HASH = "ff0b80f5e6966234a953d11c8a475c21"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_titan_predator.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_PREDATORCANNON_DESC
    WPN_LONGDESC = FRONTEND.WPN_PREDATORCANNON_LONGDESC
    WPN_NAME = FRONTEND.WPN_PREDATORCANNON_NAME


class RAILGUN(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\plasma_railgun_pr01a"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\titan_plasma_railgun"
    MATERIAL_1P_NAME_MODDED = "plasma_railgun"
    MATERIAL_1P_NAME_VANILLA = "plasma_railgun"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "atpov_titan_sniper_rifle.mdl"
    MDL_1P_FOLDER = r"models\weapons\atpov_titan_sniper_rifle"
    MDL_1P_V1_BIN = [(152088, b"\x70\x6c\x61\x73\x6d\x61\x5f\x72\x61\x69\x6c\x67\x75\x6e\x5f\x70\x72\x30\x31\x61")]
    MDL_1P_V1_BIN_VANILLA = [(152088, b"\x74\x69\x74\x61\x6e\x5f\x70\x6c\x61\x73\x6d\x61\x5f\x72\x61\x69\x6c\x67\x75\x6e")]
    MDL_1P_V1_HASH = "4ce4a1c5b8063a573db7090e4e667674"
    MDL_1P_VANILLA_HASH = "dc0ada13b2f1bf956ac4954447da4538"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_titan_sniper_rifle.mdl"
    MDL_FOLDER = "models\weapons\titan_sniper_rifle"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_RAILGUN_DESC
    WPN_LONGDESC = FRONTEND.WPN_RAILGUN_LONGDESC
    WPN_NAME = FRONTEND.WPN_RAILGUN_NAME


class THERMITECANNON(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\thermite_launcher_t203a"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\titan_thermite_launcher"
    MATERIAL_1P_NAME_MODDED = "thermite_launcher"
    MATERIAL_1P_NAME_VANILLA = "thermite_launcher"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "atpov_titan_thermite_launcher.mdl"
    MDL_1P_FOLDER = r"models\weapons\titan_thermite_launcher"
    MDL_1P_V1_BIN = [(179826, b"\x74\x68\x65\x72\x6d\x69\x74\x65\x5f\x6c\x61\x75\x6e\x63\x68\x65\x72\x5f\x74\x32\x30\x33\x61")]
    MDL_1P_V1_BIN_VANILLA = [(179826, b"\x74\x69\x74\x61\x6e\x5f\x74\x68\x65\x72\x6d\x69\x74\x65\x5f\x6c\x61\x75\x6e\x63\x68\x65\x72")]
    MDL_1P_V1_HASH = "2493a2f159146f452ec0fcaf057fe253"
    MDL_1P_VANILLA_HASH = "06dd30e9fd338ddf6448983c6053be29"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_titan_thermite_launcher.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_THERMITECANNON_DESC
    WPN_LONGDESC = FRONTEND.WPN_THERMITECANNON_LONGDESC
    WPN_NAME = FRONTEND.WPN_THERMITECANNON_NAME


class THR40MM(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\titan_50mm"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\titan_40mm"
    MATERIAL_1P_NAME_MODDED = "titan_50mm"
    MATERIAL_1P_NAME_VANILLA = "titan_40mm"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "atpov_thr_40mm.mdl"
    MDL_1P_FOLDER = r"models\weapons\thr_40mm"
    MDL_1P_V1_BIN = [
        (311945, b"\x74\x69\x74\x61\x6e\x5f\x35\x30\x6d\x6d"),
        (311956, b"\x74\x69\x74\x61\x6e\x5f\x35\x30\x6d\x6d")
    ]
    MDL_1P_V1_BIN_VANILLA = [
        (311945, b"\x74\x69\x74\x61\x6e\x5f\x34\x30\x6d\x6d"),
        (311956, b"\x74\x69\x74\x61\x6e\x5f\x34\x30\x6d\x6d")
    ]
    MDL_1P_V1_HASH = "479acbd0b9be9c1fab2f74b5fc0472ba"
    MDL_1P_VANILLA_HASH = "89207b64b421233a5903c7cd4e826765"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_thr_40mm.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_THR40MM_DESC
    WPN_LONGDESC = FRONTEND.WPN_THR40MM_LONGDESC
    WPN_NAME = FRONTEND.WPN_THR40MM_NAME


class XO16(object):
    # 1P - First person view
    MATERIAL_1P_FOLDER_MODDED = r"models\Weapons_R2\titan_chaingunbrx"
    MATERIAL_1P_FOLDER_VANILLA = r"models\Weapons_R2\xo16_shorty_titan"
    MATERIAL_1P_NAME_MODDED = "xo16a2_chaingunbr"
    MATERIAL_1P_NAME_VANILLA = "xo16_shorty_titan"
    MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
    MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
    MDL_1P_FILE = "atpov_xo16shorty.mdl"
    MDL_1P_FOLDER = r"models\weapons\titan_xo16_shorty"
    MDL_1P_V1_BIN = [
        (309859, b"\x74\x69\x74\x61\x6e\x5f\x63\x68\x61\x69\x6e\x67\x75\x6e\x62\x72\x78"),
        (309877, b"\x78\x6f\x31\x36\x61\x32\x5f\x63\x68\x61\x69\x6e\x67\x75\x6e\x62\x72")
    ]
    MDL_1P_V1_BIN_VANILLA = [
        (309859, b"\x78\x6f\x31\x36\x5f\x73\x68\x6f\x72\x74\x79\x5f\x74\x69\x74\x61\x6e"),
        (309877, b"\x78\x6f\x31\x36\x5f\x73\x68\x6f\x72\x74\x79\x5f\x74\x69\x74\x61\x6e")
    ]
    MDL_1P_V1_HASH = "3b52f3a3ddff09e69940d68e5df3474e"
    MDL_1P_VANILLA_HASH = "56e91c58b01106448dde7bf5e3c5ddcc"
    VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
    VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
    VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
    VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
    VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
    # 3P - Third person view
    MDL_FILE_3P = "w_xo16shorty.mdl"
    # FRONTEND
    WPN_DESC = FRONTEND.WPN_XO16_DESC
    WPN_LONGDESC = FRONTEND.WPN_XO16_LONGDESC
    WPN_NAME = FRONTEND.WPN_XO16_NAME


# # 1P - First person view
# MATERIAL_1P_FOLDER_MODDED = r""
# MATERIAL_1P_FOLDER_VANILLA = r""
# MATERIAL_1P_NAME_MODDED = ""
# MATERIAL_1P_NAME_VANILLA = ""
# MATERIAL_1P_PATH_MODDED = r"{0}\{1}".format(MATERIAL_1P_FOLDER_MODDED, MATERIAL_1P_NAME_MODDED)
# MATERIAL_1P_PATH_VANILLA = r"{0}\{1}".format(MATERIAL_1P_FOLDER_VANILLA, MATERIAL_1P_NAME_VANILLA)
# MDL_1P_FILE = ".mdl"
# MDL_1P_FOLDER = r""
# MDL_1P_V1_BIN = []
# MDL_1P_V1_BIN_VANILLA = []
# MDL_1P_V1_HASH = ""
# MDL_1P_VANILLA_HASH = ""
# VMT_1P_FILE = "{0}.vmt".format(MATERIAL_1P_NAME_MODDED)
# VMT_1P_FOLDER = r"materials\{0}".format(MATERIAL_1P_FOLDER_MODDED)
# VMT_1P_PATH = r"{0}\{1}".format(VMT_1P_FOLDER, VMT_1P_FILE)
# VTF_1P_AMBIENTOCC = "{0}_ambiant_occ.vtf".format(MATERIAL_1P_NAME_MODDED)
# VTF_1P_BASE = "{0}_color.vtf".format(MATERIAL_1P_NAME_MODDED)
# VTF_1P_BASE2 = "{0}_color2.vtf".format(MATERIAL_1P_NAME_MODDED)
# VTF_1P_BLENDMODULATE = "{0}_blend.vtf".format(MATERIAL_1P_NAME_MODDED)
# VTF_1P_BUMP = "{0}_normal.vtf".format(MATERIAL_1P_NAME_MODDED)
# VTF_1P_CORNEA = "{0}_cornea.vtf".format(MATERIAL_1P_NAME_MODDED)
# VTF_1P_DETAIL = "{0}_detail.vtf".format(MATERIAL_1P_NAME_MODDED)
# VTF_1P_ENV = "{0}_env.vtf".format(MATERIAL_1P_NAME_MODDED)
# VTF_1P_ENVMASK = "{0}_env_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
# VTF_1P_PHONGEXPONENT = "{0}_phong.vtf".format(MATERIAL_1P_NAME_MODDED)
# VTF_1P_SELFILLUM = "{0}_illum_mask.vtf".format(MATERIAL_1P_NAME_MODDED)
