# LPL - Local Python Libraries
from lib.core.enums import FRONTEND

# MDL_FILE_1P - First person
# MDL_FILE_3P - Third person
# MDL_FILE_HP - Holster view
# MDL_FILE_MP - Menus view
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
    MDL_FILE_1P = "ptpov_alternator_smg.mdl"
    MDL_FILE_3P = "w_alternator_smg.mdl"
    MDL_FILE_HP = "w_alternator_smg_stow.mdl"
    MDL_FOLDER = "models\\weapons\\alternator_smg"
    MDL_V1_1P = [(627836, b"\x6c"), (627851, b"\x6c")]
    MDL_V1_1P_HASH = "d472844ee12583c26d98a9018f466213"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\alternator_lmg\alternator_lmg"
    MDL_V1_1P_VANILLA = [(627836, b"\x73"), (627851, b"\x73")]
    MDL_VANILLA_1P_HASH = "e43a2964ec53f2012f388cb562f65d5b"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\alternator_smg\alternator_smg"
    WPN_DESC = FRONTEND.WPN_ALTERNATOR_DESC
    WPN_LONGDESC = FRONTEND.WPN_ALTERNATOR_LONGDESC
    WPN_NAME = FRONTEND.WPN_ALTERNATOR_NAME


class CAR101(object):
    MDL_FILE_1P = "ptpov_car101.mdl"
    MDL_FILE_3P = "w_car101.mdl"
    MDL_FOLDER = "models\\weapons\\car101"
    MDL_V1_1P = [(608664, b"\x6c"), (608672, b"\x6c")]
    MDL_V1_1P_HASH = "3a6a53a20ca444e446fbcde78aafc840"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\car_lmg\CAR_lmg"
    MDL_V1_1P_VANILLA = [(608664, b"\x73"), (608672, b"\x73")]
    MDL_VANILLA_1P_HASH = "ffafbc744228083728f29200dd426eb0"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\car_smg\CAR_smg"
    WPN_DESC = FRONTEND.WPN_CAR101_DESC
    WPN_LONGDESC = FRONTEND.WPN_CAR101_LONGDESC
    WPN_NAME = FRONTEND.WPN_CAR101_NAME


class COLDWAR(object):
    MDL_FILE_1P = "ptpov_pulse_lmg.mdl"
    MDL_FILE_3P = "w_pulse_lmg.mdl"
    MDL_FOLDER = "models\\weapons\\pulse_lmg"
    MDL_V1_1P = [
        (608664, b"\x63\x6f\x6c\x64\x34\x5f\x77\x61\x72"),
        (608672, b"\x63\x6f\x6c\x64\x34\x5f\x77\x61\x72")
    ]
    MDL_V1_1P_HASH = "dc3926c17feb465f068b8403d436d1b2"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\cold4_war\cold4_war"
    MDL_V1_1P_VANILLA = [
        (608664, b"\x70\x75\x6c\x73\x65\x5f\x6c\x6d\x67"),
        (608672, b"\x70\x75\x6c\x73\x65\x5f\x6c\x6d\x67")
    ]
    MDL_VANILLA_1P_HASH = "89402845be26fae9bc50830f59b09d82"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\pulse_lmg\pulse_lmg"
    WPN_DESC = FRONTEND.WPN_COLDWAR_DESC
    WPN_LONGDESC = FRONTEND.WPN_COLDWAR_LONGDESC
    WPN_NAME = FRONTEND.WPN_COLDWAR_NAME


class DEVOTION(object):
    MDL_FILE_1P = "ptpov_hemlock_br.mdl"
    MDL_FILE_3P = "w_hemlock_br.mdl"
    MDL_FOLDER = "models\\weapons\\hemlock_br"
    MDL_V1_1P = [
        (757105, b"\x64\x65\x76\x6f\x74\x69\x6f\x6e\x5f"),
        (757115, b"\x64\x65\x76\x6f\x74\x69\x6f\x6e\x5f")
    ]
    MDL_V1_1P_HASH = "2e7825b8f4d4015f8b3c7b684d36395c"
    MDL_V1_1P_MATERIAL = "models\weapons\devotion_\devotion_"
    MDL_V1_1P_VANILLA = [
        (757105, b"\x68\x65\x6d\x6c\x6f\x6b\x5f\x62\x72"),
        (757115, b"\x68\x65\x6d\x6c\x6f\x6b\x5f\x62\x72")
    ]
    MDL_VANILLA_1P_HASH = "5aef9f28430a805eb1172115ae4cfc0f"
    MDL_VANILLA_1P_MATERIAL = "models\weapons\hemlok_br\hemlok_br"
    WPN_DESC = FRONTEND.WPN_DEVOTION_DESC
    WPN_LONGDESC = FRONTEND.WPN_DEVOTION_LONGDESC
    WPN_NAME = FRONTEND.WPN_DEVOTION_NAME


class DOUBLETAKE(object):
    MDL_FILE_1P = "ptpov_doubletake.mdl"
    MDL_FILE_3P = "w_doubletake.mdl"
    MDL_FOLDER = "models\\weapons\\doubletake"
    MDL_V1_1P = [
        (942419, b"\x74\x72\x69\x70\x6c\x65\x74\x61\x6b\x65\x5f\x73\x72"),
        (942433, b"\x74\x72\x69\x70\x6c\x65\x74\x61\x6b\x65")
    ]
    MDL_V1_1P_HASH = "d75873936045bb813039ca86160b0d1b"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\tripletake_sr\tripletake"
    MDL_V1_1P_VANILLA = [
        (942419, b"\x64\x6f\x75\x62\x6c\x65\x74\x61\x6b\x65\x5f\x73\x72"),
        (942433, b"\x64\x6f\x75\x62\x6c\x65\x74\x61\x6b\x65")
    ]
    MDL_VANILLA_1P_HASH = "a6cd5d0fab1764cf9158cce06a71f6ff"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\doubletake_sr\doubletake"
    WPN_DESC = FRONTEND.WPN_DOUBLETAKE_DESC
    WPN_LONGDESC = FRONTEND.WPN_DOUBLETAKE_LONGDESC
    WPN_NAME = FRONTEND.WPN_DOUBLETAKE_NAME


class EPG(object):
    MDL_FILE_1P = "ptpov_epg.mdl"
    MDL_FILE_3P = "w_epg.mdl"
    MDL_FOLDER = "models\\weapons\\epg"
    MDL_V1_1P = [(610289, b"\x65\x70\x6a"), (610293, b"\x65\x70\x6a")]
    MDL_V1_1P_HASH = "22c2c99fb5a846dfc7e2f1d039438b46"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\epj\epj"
    MDL_V1_1P_VANILLA = [(610289, b"\x65\x70\x67"), (610293, b"\x65\x70\x67")]
    MDL_VANILLA_1P_HASH = "a94e174bdb8dfea78b779dae66ef3cdf"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\epg\epg"
    WPN_DESC = FRONTEND.WPN_EPG_DESC
    WPN_LONGDESC = FRONTEND.WPN_EPG_LONGDESC
    WPN_NAME = FRONTEND.WPN_EPG_NAME


class EVA8(object):
    MDL_FILE_1P = "ptpov_w1128.mdl"
    MDL_FILE_3P = "w_w1128.mdl"
    MDL_FOLDER = "models\\weapons\\w1128"
    MDL_V1_1P = [(563204, b"\x37"), (563214, b"\x37")]
    MDL_V1_1P_HASH = "1425b759dfd05dc59cdf804d74d57f67"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\eva7_stgn\eva7_stgn"
    MDL_V1_1P_VANILLA = [(563204, b"\x38"), (563214, b"\x38")]
    MDL_VANILLA_1P_HASH = "f09961f7d9bb15b12ac3aed23b8b5aac"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\eva8_stgn\eva8_stgn"
    WPN_DESC = FRONTEND.WPN_EVA8_DESC
    WPN_LONGDESC = FRONTEND.WPN_EVA8_LONGDESC
    WPN_NAME = FRONTEND.WPN_EVA8_NAME


class FLATLINE(object):
    MDL_FILE_1P = "ptpov_vinson.mdl"
    MDL_FILE_3P = "w_vinson.mdl"
    MDL_FOLDER = "models\\weapons\\vinson"
    MDL_V1_1P = [
        (639230, b"\x66\x6c\x61\x74\x6c\x69\x6e\x65\x5f\x61\x72\x66")
    ]
    MDL_V1_1P_HASH = "d45a13b7b66eaa4e59a99d34fc8f2829"
    MDL_V1_1P_MATERIAL = "models\weapons\vinson\flatline_arf"
    MDL_V1_1P_VANILLA = [
        (639230, b"\x76\x69\x6e\x73\x6f\x6e\x5f\x72\x69\x66\x6c\x65")
    ]
    MDL_VANILLA_1P_HASH = "d85f1d546dec75fad24e884bd6ab2101"
    MDL_VANILLA_1P_MATERIAL = "models\weapons\vinson\vinson_rifle"
    WPN_DESC = FRONTEND.WPN_FLATLINE_DESC
    WPN_LONGDESC = FRONTEND.WPN_FLATLINE_LONGDESC
    WPN_NAME = FRONTEND.WPN_FLATLINE_NAME


class G2A5(object):
    MDL_FILE_1P = "ptpov_g2a4.mdl"
    MDL_FILE_3P = "w_g2a4.mdl"
    MDL_FOLDER = "models\\weapons\\g2"
    MDL_V1_1P = [(616532, b"\x35"), (616540, b"\x35")]
    MDL_V1_1P_HASH = "ede7dad905e40d2b3aa4982562e1180f"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\g2a5_ar\g2a5_ar"
    MDL_V1_1P_VANILLA = [(616532, b"\x34"), (616540, b"\x34")]
    MDL_VANILLA_1P_HASH = "c47c07d1646a6f7921f34e1d38ebbe69"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\g2a4_ar\g2a4_ar"
    WPN_DESC = FRONTEND.WPN_G2A5_DESC
    WPN_LONGDESC = FRONTEND.WPN_G2A5_LONGDESC
    WPN_NAME = FRONTEND.WPN_G2A5_NAME


class HEMLOK(object):
    MDL_FILE_1P = "ptpov_hemlok.mdl"
    MDL_FILE_3P = "w_hemlok.mdl"
    MDL_FOLDER = "models\\weapons\\m1a1_hemlok"
    MDL_V1_1P = [(646701, b"\x63"), (646715, b"\x63\x66\x72")]
    MDL_V1_1P_HASH = "3d72fde9b8db290ffc22b9a264d946cf"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\hemlok_cfr_ar\hemlok_cfr_ar"
    MDL_V1_1P_VANILLA = [(646701, b"\x62"), (646715, b"\x42\x46\x52")]
    MDL_VANILLA_1P_HASH = "d2a1e67c84860bfc312b03c19f26d814"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\hemlok_bfr_ar\hemlok_BFR_ar"
    WPN_DESC = FRONTEND.WPN_HEMLOK_DESC
    WPN_LONGDESC = FRONTEND.WPN_HEMLOK_LONGDESC
    WPN_NAME = FRONTEND.WPN_HEMLOK_NAME


class KRABER(object):
    MDL_FILE_1P = "ptpov_at_rifle.mdl"
    MDL_FILE_3P = "w_at_rifle.mdl"
    MDL_FOLDER = "models\\weapons\\at_rifle"
    MDL_V1_1P = [(861702, b"\x74"), (861712, b"\x74")]
    MDL_V1_1P_HASH = "237e66e221119e3cc07a6ab2647a3468"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\kraber_tr\kraber_tr"
    MDL_V1_1P_VANILLA = [(861702, b"\x73"), (861712, b"\x73")]
    MDL_VANILLA_1P_HASH = "a59db6a8942348dadab434a5eb22c818"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\kraber_sr\kraber_sr"
    WPN_DESC = FRONTEND.WPN_KRABER_DESC
    WPN_LONGDESC = FRONTEND.WPN_KRABER_LONGDESC
    WPN_NAME = FRONTEND.WPN_KRABER_NAME


class LONGBOW(object):
    MDL_FILE_1P = "ptpov_rspn101_dmr.mdl"
    MDL_FILE_3P = "w_rspn101_dmr.mdl"
    MDL_FOLDER = "models\\weapons\\rspn101_dmr"
    MDL_V1_1P = [(624410, b"\x6c"), (624418, b"\x63"), (624430, b"\x63")]
    MDL_V1_1P_HASH = "133a4cd435329a4f6e80f297c802bd15"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\longbow_cmr\longbow_cmr"
    MDL_V1_1P_VANILLA = [(624410, b"\x4c"), (624418, b"\x64"), (624430, b"\x64")]
    MDL_VANILLA_1P_HASH = "b1dce9fefe55ba03a779bca98c21ea18"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\Longbow_dmr\longbow_dmr"
    WPN_DESC = FRONTEND.WPN_LONGBOW_DESC
    WPN_LONGDESC = FRONTEND.WPN_LONGBOW_LONGDESC
    WPN_NAME = FRONTEND.WPN_LONGBOW_NAME


class LSTAR(object):
    MDL_FILE_1P = "ptpov_lstar.mdl"
    MDL_FILE_3P = "w_lstar.mdl"
    MDL_FILE_HP = "w_lstar_stow.mdl"
    MDL_FILE_MP = "ptpov_lstar_menu.mdl"
    MDL_FOLDER = "models\\weapons\\lstar"
    MDL_V1_1P = [(1059670, b"\x73"), (1059676, b"\x73")]
    MDL_V1_1P_HASH = "f4b4c270cf8d0849acb053ec379a7a30"
    MDL_V1_1P_MATERIAL = "models\weapons\lstas\lstas"
    MDL_V1_1P_VANILLA = [(1059670, b"\x72"), (1059676, b"\x72")]
    MDL_VANILLA_1P_HASH = "e774bd7ed35c2fc06a43d61a8d659d1c"
    MDL_VANILLA_1P_MATERIAL = "models\weapons\lstar\lstar"
    WPN_DESC = FRONTEND.WPN_LSTAR_DESC
    WPN_LONGDESC = FRONTEND.WPN_LSTAR_LONGDESC
    WPN_NAME = FRONTEND.WPN_LSTAR_NAME


class MASTIFF(object):
    MDL_FILE_1P = "ptpov_mastiff.mdl"
    MDL_FILE_3P = "w_mastiff.mdl"
    MDL_FOLDER = "models\\weapons\\mastiff_stgn"
    MDL_V1_1P = [(555217, b"\x6f"), (555230, b"\x6f")]
    MDL_V1_1P_HASH = "dd2d31da0d1dad3af7459b7c61812892"
    MDL_V1_1P_MATERIAL = "models\weapons\mastiff_stgo\mastiff_stgo"
    MDL_V1_1P_VANILLA = [(555217, b"\x6e"), (555230, b"\x6e")]
    MDL_VANILLA_1P_HASH = "822241de8ed57fa76fea708937bab58e"
    MDL_VANILLA_1P_MATERIAL = "models\weapons\mastiff_stgn\mastiff_stgn"
    WPN_DESC = FRONTEND.WPN_MASTIFF_DESC
    WPN_LONGDESC = FRONTEND.WPN_MASTIFF_LONGDESC
    WPN_NAME = FRONTEND.WPN_MASTIFF_NAME


class R101(object):
    MDL_FILE_1P = "ptpov_r101_sfp.mdl"
    MDL_FILE_3P = "w_r101_sfp.mdl"
    MDL_FILE_HP = "w_r101_sfp_stow.mdl"
    MDL_FOLDER = "models\\weapons\\r101_sfp"
    MDL_V1_1P = [(685216, b"\x74"), (685225, b"\x74")]
    MDL_V1_1P_HASH = "f1a3ac597acce4c222e73fbac8289129"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\r101_tfp\r101_tfp"
    MDL_V1_1P_VANILLA = [(685216, b"\x73"), (685225, b"\x73")]
    MDL_VANILLA_1P_HASH = "d19bfa83ea1703c34309cda246e34194"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\r101_sfp\r101_sfp"
    WPN_DESC = FRONTEND.WPN_R101_DESC
    WPN_LONGDESC = FRONTEND.WPN_R101_LONGDESC
    WPN_NAME = FRONTEND.WPN_R101_NAME


class R201(object):
    MDL_FILE_1P = "ptpov_rspn101.mdl"
    MDL_FILE_3P = "w_rspn101.mdl"
    MDL_FILE_HP = "w_rspn101_stow.mdl"
    MDL_FOLDER = "models\\weapons\\rspn101"
    MDL_V1_1P = [(609696, b"\x32"), (609701, b"\x32")]
    MDL_V1_1P_HASH = "7a965893366faa33f5d833dbf4b3af96"
    MDL_V1_1P_MATERIAL = "models\weapons\r101\r101"
    MDL_V1_1P_VANILLA = [(609696, b"\x31"), (609701, b"\x31")]
    MDL_VANILLA_1P_HASH = "02ca186fb737666b78d29b6938c71c40"
    MDL_VANILLA_1P_MATERIAL = "models\weapons\r101\r101"
    WPN_DESC = FRONTEND.WPN_R201_DESC
    WPN_LONGDESC = FRONTEND.WPN_R201_LONGDESC
    WPN_NAME = FRONTEND.WPN_R201_NAME


class R97(object):
    MDL_FILE_1P = "ptpov_r97.mdl"
    MDL_FILE_3P = "w_r97.mdl"
    MDL_FOLDER = "models\\weapons\\r97"
    MDL_V1_1P = [(596425, b"\x38"), (596427, b"\x72\x39\x38\x5f\x63\x6e")]
    MDL_V1_1P_HASH = "33a8695df765a26cea87112bf870ea34"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\r98\r98_cn"
    MDL_V1_1P_VANILLA = [(596425, b"\x37"), (596427, b"\x52\x39\x37\x5f\x43\x4e")]
    MDL_VANILLA_1P_HASH = "854d5f860b97bfdd31ba42f2cc5b0de7"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\r97\R97_CN"
    WPN_DESC = FRONTEND.WPN_R97_DESC
    WPN_LONGDESC = FRONTEND.WPN_R97_LONGDESC
    WPN_NAME = FRONTEND.WPN_R97_NAME


class SMR(object):
    MDL_FILE_1P = "ptpov_ARL.mdl"
    MDL_FILE_3P = "w_ARL.mdl"
    MDL_FOLDER = "models\\weapons\\auto_rocket_launcher_ARL"
    MDL_V1_1P = [(869909, b"\x6d\x72"), (869923, b"\x6d\x72")]
    MDL_V1_1P_HASH = "4c62440b097dc4e401db39ccb386e003"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\sidewinder_mr\sidewinder_mr"
    MDL_V1_1P_VANILLA = [(869909, b"\x61\x74"), (869923, b"\x61\x74")]
    MDL_VANILLA_1P_HASH = "616ffb2b1e3fc23bc2f1cc69d1932876"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\sidewinder_at\sidewinder_at"
    WPN_DESC = FRONTEND.WPN_SMR_DESC
    WPN_LONGDESC = FRONTEND.WPN_SMR_LONGDESC
    WPN_NAME = FRONTEND.WPN_SMR_NAME


class SOFTBALL(object):
    MDL_FILE_1P = "ptpov_softball_at.mdl"
    MDL_FILE_3P = "w_softball_at.mdl"
    MDL_FOLDER = "models\\weapons\\softball_at"
    MDL_V1_1P = [(451899, b"\x6d\x72"), (451911, b"\x6d\x72")]
    MDL_V1_1P_HASH = "b9755febe59e42fe70e1c5fc535d7917"
    MDL_V1_1P_MATERIAL = "models\weapons\softball_at\softball_at_skin01"
    MDL_V1_1P_VANILLA = [(451899, b"\x61\x74"), (451911, b"\x61\x74")]
    MDL_VANILLA_1P_HASH = "7e49257738fc45a257f7b979f8c4a083"
    MDL_VANILLA_1P_MATERIAL = "models\weapons\softball_at\softball_at_skin01"
    WPN_DESC = FRONTEND.WPN_SOFTBALL_DESC
    WPN_LONGDESC = FRONTEND.WPN_SOFTBALL_LONGDESC
    WPN_NAME = FRONTEND.WPN_SOFTBALL_NAME


class SPITFIRE(object):
    MDL_FILE_1P = "ptpov_lmg_hemlok.mdl"
    MDL_FILE_3P = "w_lmg_hemlok.mdl"
    MDL_FOLDER = "models\\weapons\\lmg_hemlok"
    MDL_V1_1P = [(682288, b"\x73"), (682301, b"\x73")]
    MDL_V1_1P_HASH = "5373576625b93574398a8ef12e610ade"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\spitfire_lmg\spitfire_lmg"
    MDL_V1_1P_VANILLA = [(682288, b"\x6c"), (682301, b"\x6c")]
    MDL_VANILLA_1P_HASH = "8eb642219eb5f0c610d16f30dc72ced0"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\spitfire_lmg\spitfire_lmg"
    WPN_DESC = FRONTEND.WPN_SPITFIRE_DESC
    WPN_LONGDESC = FRONTEND.WPN_SPITFIRE_LONGDESC
    WPN_NAME = FRONTEND.WPN_SPITFIRE_NAME


class VOLT(object):
    MDL_FILE_1P = "ptpov_hemlok_smg.mdl"
    MDL_FILE_3P = "w_hemlok_smg.mdl"
    MDL_FOLDER = "models\\weapons\\hemlok_smg"
    MDL_V1_1P = [
        (629644, b"\x76\x6f\x6c\x74\x62\x72\x64"),
        (629655, b"\x76\x6f\x6c\x74\x62\x72\x64"),
    ]
    MDL_V1_1P_HASH = "db36d9682c1fb4af95cac9284a97a4c6"
    MDL_V1_1P_MATERIAL = "models\weapons\hemlok_smg\voltbrd_smg"
    MDL_V1_1P_VANILLA = [
        (629644, b"\x68\x65\x6d\x6c\x6f\x63\x6b"),
        (629655, b"\x68\x65\x6d\x6c\x6f\x63\x6b"),
    ]
    MDL_VANILLA_1P_HASH = "f45f9c9262cc36a70157d4dc8599ba83"
    MDL_VANILLA_1P_MATERIAL = "models\weapons\hemlok_smg\hemlock_smg"
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
    MDL_FILE_1P = "ptpov_pstl_sa3.mdl"
    MDL_FILE_3P = "w_pstl_sa3.mdl"
    MDL_FOLDER = "models\\weapons\\pstl_sa3"
    MDL_V1_1P = [
        (579114, b"\x6d\x6f\x7a\x61\x6d\x62\x69\x71"),
        (579123, b"\x6d\x6f\x7a\x61\x6d\x62\x69\x71")
    ]
    MDL_V1_1P_HASH = "431afd05d29a9d2e8cf8b013304b7d48"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\mozambiq\mozambiq"
    MDL_V1_1P_VANILLA = [
        (579114, b"\x70\x73\x74\x6c\x5f\x73\x61\x33"),
        (579123, b"\x70\x73\x74\x6c\x5f\x73\x61\x33")
    ]
    MDL_VANILLA_1P_HASH = "8756547f29f3aaa2c4005c1cd374d0f4"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\pstl_sa3\pstl_sa3"
    WPN_DESC = FRONTEND.WPN_MOZAMBIQUE_DESC
    WPN_LONGDESC = FRONTEND.WPN_MOZAMBIQUE_LONGDESC
    WPN_NAME = FRONTEND.WPN_MOZAMBIQUE_NAME


class P2016(object):
    MDL_FILE_1P = "ptpov_p2011.mdl"
    MDL_FILE_3P = "w_p2011.mdl"
    MDL_FOLDER = "models\\weapons\\p2011"
    MDL_V1_1P = [(598042, b"\x36"), (598049, b"\x70"), (598053, b"\x36")]
    MDL_V1_1P_HASH = "edd97c77a57b0e407adde7cab767e65a"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\p2016_pstl\p2016_pstl"
    MDL_V1_1P_VANILLA = [(598042, b"\x31"), (598049, b"\x50"), (598053, b"\x31")]
    MDL_VANILLA_1P_HASH = "2276773f7437bde4fb1e0e5cf14ea4d9"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\p2011_pstl\P2011_pstl"
    WPN_DESC = FRONTEND.WPN_P2016_DESC
    WPN_LONGDESC = FRONTEND.WPN_P2016_LONGDESC
    WPN_NAME = FRONTEND.WPN_P2016_NAME


class RE45(object):
    MDL_FILE_1P = "ptpov_p2011_auto.mdl"
    MDL_FILE_3P = "w_p2011_auto.mdl"
    MDL_FOLDER = "models\\weapons\\p2011_auto"
    MDL_V1_1P = [
        (688694, b"\x72\x65\x65\x65\x65\x65\x65\x65\x65"),
        (688704, b"\x72\x65\x34\x35"),
    ]
    MDL_V1_1P_HASH = "a8177fa9741568e6060cd2a4e5de244c"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\reeeeeeee\re45"
    MDL_V1_1P_VANILLA = [
        (688694, b"\x72\x65\x34\x35\x5f\x70\x73\x74\x6c"),
        (688704, b"\x52\x45\x34\x35"),
    ]
    MDL_VANILLA_1P_HASH = "3e1e77129d75ac5f74f0bfa30dfcae41"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\re45_pstl\RE45"
    WPN_DESC = FRONTEND.WPN_RE45_DESC
    WPN_LONGDESC = FRONTEND.WPN_RE45_LONGDESC
    WPN_NAME = FRONTEND.WPN_RE45_NAME


class SMARTPISTOL(object):
    MDL_FILE_1P = "ptpov_p2011sp.mdl"
    MDL_FILE_3P = "w_p2011sp.mdl"
    MDL_FOLDER = "models\\weapons\\p2011sp"
    MDL_V1_1P = [
        (564963, b"\x69\x64\x69\x6f\x74"),
        (564976, b"\x69\x64\x69\x6f\x74\x5f\x70\x69\x73\x74\x6f\x6c\x5f\x6d\x6b\x37\x0a")
    ]
    MDL_V1_1P_HASH = "e8c8a7dc8405548a4d9436570093132e"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\idiot_pistol\idiot_pistol_mk7"
    MDL_V1_1P_VANILLA = [
        (564963, b"\x73\x6d\x61\x72\x74"),
        (564976, b"\x53\x6d\x61\x72\x74\x5f\x50\x69\x73\x74\x6f\x6c\x5f\x4d\x4b\x36\x0a")
    ]
    MDL_VANILLA_1P_HASH = "362e8289fee575f4ac5b2c62e84fae6e"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\smart_pistol\Smart_Pistol_MK6"
    WPN_DESC = FRONTEND.WPN_SMARTPISTOL_DESC
    WPN_LONGDESC = FRONTEND.WPN_SMARTPISTOL_LONGDESC
    WPN_NAME = FRONTEND.WPN_SMARTPISTOL_NAME


class WINGMANB3(object):
    MDL_FILE_1P = "ptpov_b3wing.mdl"
    MDL_FILE_3P = "w_b3wing.mdl"
    MDL_FOLDER = "models\\weapons\\b3wing"
    MDL_V1_1P = [(699297, b"\x62\x33\x6f\x67"), (699310, b"\x62\x33\x6f\x67")]
    MDL_V1_1P_HASH = "8c99ce2feee6dd7ba93dc22a04454f31"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\wingman_b3og\wingman_b3og"
    MDL_V1_1P_VANILLA = [(699297, b"\x70\x73\x74\x6c"), (699310, b"\x70\x73\x74\x6c")]
    MDL_VANILLA_1P_HASH = "967c4cd2c02e2d0e6fc968a0dd73e170"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\wingman_pstl\wingman_pstl"
    WPN_DESC = FRONTEND.WPN_WINGMANB3_DESC
    WPN_LONGDESC = FRONTEND.WPN_WINGMANB3_LONGDESC
    WPN_NAME = FRONTEND.WPN_WINGMANB3_NAME


class WINGMANN(object):
    MDL_FILE_1P = "ptpov_wingman_elite.mdl"
    MDL_FILE_3P = "w_wingman_elite.mdl"
    MDL_FOLDER = "models\\weapons\\wingman_elite"
    MDL_V1_1P = [
        (681622, b"\x65\x6c\x70\x72\x6f"),
        (681636, b"\x65\x6c\x70\x72\x6f")
    ]
    MDL_V1_1P_HASH = "5ae1e68e104b717e532de579a24351c2"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\wingman_elpro\wingman_elpro"
    MDL_V1_1P_VANILLA = [
        (681622, b"\x65\x6c\x69\x74\x65"),
        (681636, b"\x65\x6c\x69\x74\x65")
    ]
    MDL_VANILLA_1P_HASH = "92ae5f18b5576a285a1f8b2ad4be283d"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\wingman_elite\wingman_elite"
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
    MDL_FILE_1P = "ptpov_law.mdl"
    MDL_FILE_3P = "w_shoulder_rocket_SRAM_v2.mdl"
    MDL_FILE_HP = "w_rocket_SRAM_v2_stow.mdl"
    MDL_FOLDER = "models\\weapons\\shoulder_rocket_SRAM"
    MDL_V1_1P = [(667881, b"\x73\x72"), (667891, b"\x73\x72")]
    MDL_V1_1P_HASH = "bec2aa2f24f7e58809645fd07e42a78e"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\archer_sr\archer_sr"
    MDL_V1_1P_VANILLA = [(667881, b"\x61\x74"), (667891, b"\x61\x74")]
    MDL_VANILLA_1P_HASH = "1ff33d9dd106cac914dbdee9fee3b1e2"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\archer_at\archer_at"
    WPN_DESC = FRONTEND.WPN_ARCHER_DESC
    WPN_LONGDESC = FRONTEND.WPN_ARCHER_LONGDESC
    WPN_NAME = FRONTEND.WPN_ARCHER_NAME


class DEFENDER(object):
    MDL_FILE_1P = "ptpov_defender.mdl"
    MDL_FILE_3P = "w_defender.mdl"
    MDL_FILE_HP = "w_defender_stow.mdl"
    MDL_FOLDER = "models\\weapons\\defender"
    MDL_V1_1P = [
        (486358, b"\x6c\x61\x73\x65\x72"),
        (486371, b"\x6c\x61\x73\x65\x72\x5f\x73\x72")
    ]
    MDL_V1_1P_HASH = "6b5ef387fc6fb376764ac07f2833a3f1"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\charge_laser\charge_laser_sr"
    MDL_V1_1P_VANILLA = [
        (486358, b"\x72\x69\x66\x6c\x65"),
        (486371, b"\x72\x69\x66\x6c\x65\x5f\x61\x74")
    ]
    MDL_VANILLA_1P_HASH = "ba5c6f576f75df13af2a57b519657924"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\charge_rifle\charge_rifle_at"
    WPN_DESC = FRONTEND.WPN_DEFENDER_DESC
    WPN_LONGDESC = FRONTEND.WPN_DEFENDER_LONGDESC
    WPN_NAME = FRONTEND.WPN_DEFENDER_NAME


class MGL(object):
    MDL_FILE_1P = "ptpov_mgl_at.mdl"
    MDL_FILE_3P = "w_mgl_at.mdl"
    MDL_FILE_HP = "w_mgl_at_stow.mdl"
    MDL_FOLDER = "models\\weapons\\mgl_at"
    MDL_V1_1P = [(1356238, b"\x72"), (1356245, b"\x72")]
    MDL_V1_1P_HASH = "2c6de5b83a19915a559497d22a892fbd"
    MDL_V1_1P_MATERIAL = "models\weapons\mgl_ar\mgl_ar"
    MDL_V1_1P_VANILLA = [(1356238, b"\x74"), (1356245, b"\x74")]
    MDL_VANILLA_1P_HASH = "5ee122587f96931c31f76e51cf6c6aba"
    MDL_VANILLA_1P_MATERIAL = "models\weapons\mgl_at\mgl_at"
    WPN_DESC = FRONTEND.WPN_MGL_DESC
    WPN_LONGDESC = FRONTEND.WPN_MGL_LONGDESC
    WPN_NAME = FRONTEND.WPN_MGL_NAME


class THUNDERBOLT(object):
    MDL_FILE_1P = "ptpov_arc_launcher.mdl"
    MDL_FILE_3P = "w_arc_launcher.mdl"
    MDL_FILE_HP = "w_arc_launcher_stow.mdl"
    MDL_FOLDER = "models\\weapons\\arc_launcher"
    MDL_V1_1P = [
        (519557, b"\x74\x68\x75\x6e\x64\x65\x72\x62\x6f\x6c\x74\x5f"),
        (519570, b"\x74\x68\x75\x6e\x64\x65\x72\x62\x6f\x6c\x74\x5f")
    ]
    MDL_V1_1P_HASH = "4c4a0813d390c0b3ff0c2af891a9d915"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\thunderbolt_\thunderbolt_"
    MDL_V1_1P_VANILLA = [
        (519557, b"\x61\x72\x63\x5f\x6c\x61\x75\x6e\x63\x68\x65\x72"),
        (519570, b"\x61\x72\x63\x5f\x6c\x61\x75\x6e\x63\x68\x65\x72")
    ]
    MDL_VANILLA_1P_HASH = "c18ad176d9195e49034817b5aa5327d0"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\arc_launcher\arc_launcher"
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
    MDL_FILE_1P = "atpov_titan_triple_threat.mdl"
    MDL_FILE_3P = "w_titan_triple_threat.mdl"
    MDL_FOLDER = "models\\weapons\\titan_triple_threat"
    MDL_V1_1P = [
        (130666, b"\x6c\x65\x61\x64\x77\x61\x6c\x6c\x5f\x73\x74\x67\x6e"),
        (130680, b"\x6c\x65\x61\x64\x77\x61\x6c\x6c\x5f\x73\x74\x67\x6e")
    ]
    MDL_V1_1P_HASH = "f5eb2d8c4e0e6eca951271f80c17496e"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\titan_leadwall_stgn\leadwall_stgn"
    MDL_V1_1P_VANILLA = [
        (130666, b"\x74\x72\x69\x70\x6c\x65\x5f\x74\x68\x72\x65\x61\x74"),
        (130680, b"\x74\x72\x69\x70\x6c\x65\x5f\x74\x68\x72\x65\x61\x74")
    ]
    MDL_VANILLA_1P_HASH = "0d3a45aff637d3cc5ac4442162679a01"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\titan_triple_threat\triple_threat"
    WPN_DESC = FRONTEND.WPN_LEADWALL_DESC
    WPN_LONGDESC = FRONTEND.WPN_LEADWALL_LONGDESC
    WPN_NAME = FRONTEND.WPN_LEADWALL_NAME


class PARTICLEACCELERATOR(object):
    MDL_FILE_1P = "atpov_titan_particle_accelerator.mdl"
    MDL_FILE_3P = "w_titan_particle_accelerator.mdl"
    MDL_FOLDER = "models\\weapons\\titan_particle_accelerator"
    MDL_V1_1P = [
        (358654, b"\x73\x70\x6c\x69\x74\x74\x65\x72"),
        (358681, b"\x73\x70\x6c\x69\x74\x74\x65\x72")
    ]
    MDL_V1_1P_HASH = "e8b59cd2af6b4cafe76f2f4a0c660fed"
    MDL_V1_1P_MATERIAL = "models\weapons\titan_splitter_accelerator\titan_splitter_accelerator"
    MDL_V1_1P_VANILLA = [
        (358654, b"\x70\x61\x72\x74\x69\x63\x6c\x65"),
        (358681, b"\x70\x61\x72\x74\x69\x63\x6c\x65")
    ]
    MDL_VANILLA_1P_HASH = "f945aa95740aac99d108a96a61a53521"
    MDL_VANILLA_1P_MATERIAL = "models\weapons\titan_particle_accelerator\titan_particle_accelerator"
    WPN_DESC = FRONTEND.WPN_PARTICLEACCELERATOR_DESC
    WPN_LONGDESC = FRONTEND.WPN_PARTICLEACCELERATOR_LONGDESC
    WPN_NAME = FRONTEND.WPN_PARTICLEACCELERATOR_NAME


class PREDATORCANNON(object):
    MDL_FILE_1P = "atpov_titan_predator.mdl"
    MDL_FILE_3P = "w_titan_predator.mdl"
    MDL_FOLDER = "models\\weapons\\titan_predator"
    MDL_V1_1P = [
        (376528, b"\x67\x61\x74\x6c\x69"),
        (376543, b"\x67\x61\x74\x6c\x69")
    ]
    MDL_V1_1P_HASH = "ed556151e9d4b9f44337602c4c387925"
    MDL_V1_1P_MATERIAL = "models\weapons\predator_gatli\predator_gatli"
    MDL_V1_1P_VANILLA = [
        (376528, b"\x74\x69\x74\x61\x6e"),
        (376543, b"\x74\x69\x74\x61\x6e")
    ]
    MDL_VANILLA_1P_HASH = "ff0b80f5e6966234a953d11c8a475c21"
    MDL_VANILLA_1P_MATERIAL = "models\weapons\predator_titan\predator_titan"
    WPN_DESC = FRONTEND.WPN_PREDATORCANNON_DESC
    WPN_LONGDESC = FRONTEND.WPN_PREDATORCANNON_LONGDESC
    WPN_NAME = FRONTEND.WPN_PREDATORCANNON_NAME


class RAILGUN(object):
    MDL_FILE_1P = "atpov_titan_sniper_rifle.mdl"
    MDL_FILE_3P = "w_titan_sniper_rifle.mdl"
    MDL_FOLDER = "models\\weapons\\atpov_titan_sniper_rifle"
    MDL_FOLDER2 = "models\\weapons\\titan_sniper_rifle"
    MDL_V1_1P = [(152088, b"\x70\x6c\x61\x73\x6d\x61\x5f\x72\x61\x69\x6c\x67\x75\x6e\x5f\x70\x72\x30\x31\x61")]
    MDL_V1_1P_HASH = "4ce4a1c5b8063a573db7090e4e667674"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\plasma_railgun_pr01a\plasma_railgun"
    MDL_V1_1P_VANILLA = [(152088, b"\x74\x69\x74\x61\x6e\x5f\x70\x6c\x61\x73\x6d\x61\x5f\x72\x61\x69\x6c\x67\x75\x6e")]
    MDL_VANILLA_1P_HASH = "dc0ada13b2f1bf956ac4954447da4538"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\titan_plasma_railgun\plasma_railgun"
    WPN_DESC = FRONTEND.WPN_RAILGUN_DESC
    WPN_LONGDESC = FRONTEND.WPN_RAILGUN_LONGDESC
    WPN_NAME = FRONTEND.WPN_RAILGUN_NAME


class THERMITECANNON(object):
    MDL_FILE_1P = "atpov_titan_thermite_launcher.mdl"
    MDL_FILE_3P = "w_titan_thermite_launcher.mdl"
    MDL_FOLDER = "models\\weapons\\titan_thermite_launcher"
    MDL_V1_1P = [(179826, b"\x74\x68\x65\x72\x6d\x69\x74\x65\x5f\x6c\x61\x75\x6e\x63\x68\x65\x72\x5f\x74\x32\x30\x33\x61")]
    MDL_V1_1P_HASH = "models\Weapons_R2\thermite_launcher_t203a\thermite_launcher"
    MDL_V1_1P_MATERIAL = "2493a2f159146f452ec0fcaf057fe253"
    MDL_V1_1P_VANILLA = [(179826, b"\x74\x69\x74\x61\x6e\x5f\x74\x68\x65\x72\x6d\x69\x74\x65\x5f\x6c\x61\x75\x6e\x63\x68\x65\x72")]
    MDL_VANILLA_1P_HASH = "06dd30e9fd338ddf6448983c6053be29"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\titan_thermite_launcher\thermite_launcher"
    WPN_DESC = FRONTEND.WPN_THERMITECANNON_DESC
    WPN_LONGDESC = FRONTEND.WPN_THERMITECANNON_LONGDESC
    WPN_NAME = FRONTEND.WPN_THERMITECANNON_NAME


class THR40MM(object):
    MDL_FILE_1P = "atpov_thr_40mm.mdl"
    MDL_FILE_3P = "w_thr_40mm.mdl"
    MDL_FOLDER = "models\\weapons\\thr_40mm"
    MDL_V1_1P = [
        (311945, b"\x34\x30\x6d\x6d\x5f\x68\x61\x75\x72\x64"),
        (311956, b"\x34\x30\x6d\x6d\x5f\x68\x61\x75\x72\x64")
    ]
    MDL_V1_1P_HASH = "be5296f004692a5c5e38c2b7375347b2"
    MDL_V1_1P_MATERIAL = "models\Weapons_R2\40mm_haurd\40mm_haurd"
    MDL_V1_1P_VANILLA = [
        (311945, b"\x74\x69\x74\x61\x6e\x5f\x34\x30\x6d\x6d"),
        (311956, b"\x74\x69\x74\x61\x6e\x5f\x34\x30\x6d\x6d")
    ]
    MDL_VANILLA_1P_HASH = "89207b64b421233a5903c7cd4e826765"
    MDL_VANILLA_1P_MATERIAL = "models\Weapons_R2\titan_40mm\titan_40mm"
    WPN_DESC = FRONTEND.WPN_THR40MM_DESC
    WPN_LONGDESC = FRONTEND.WPN_THR40MM_LONGDESC
    WPN_NAME = FRONTEND.WPN_THR40MM_NAME


class XO16(object):
    MDL_FILE_1P = "atpov_xo16shorty.mdl"
    MDL_FILE_3P = "w_xo16shorty.mdl"
    MDL_FOLDER = "models\\weapons\\titan_xo16_shorty"
    MDL_V1_1P = [
        (309859, b"\x78\x6f\x31\x36\x61\x32\x5f\x63\x68\x61\x69\x6e\x67\x75\x6e\x62\x72"),
        (309877, b"\x78\x6f\x31\x36\x61\x32\x5f\x63\x68\x61\x69\x6e\x67\x75\x6e\x62\x72")
    ]
    MDL_V1_1P_HASH = "ad90df5a99178aec65b56814b09a1185"
    MDL_V1_1P_MATERIAL = r"models\Weapons_R2\xo16a2_chaingunbr\xo16a2_chaingunbr"
    MDL_V1_1P_VANILLA = [
        (309859, b"\x78\x6f\x31\x36\x5f\x73\x68\x6f\x72\x74\x79\x5f\x74\x69\x74\x61\x6e"),
        (309877, b"\x78\x6f\x31\x36\x5f\x73\x68\x6f\x72\x74\x79\x5f\x74\x69\x74\x61\x6e")
    ]
    MDL_VANILLA_1P_HASH = "56e91c58b01106448dde7bf5e3c5ddcc"
    MDL_VANILLA_1P_MATERIAL = r"models\Weapons_R2\xo16_shorty_titan\xo16_shorty_titan"
    WPN_DESC = FRONTEND.WPN_XO16_DESC
    WPN_LONGDESC = FRONTEND.WPN_XO16_LONGDESC
    WPN_NAME = FRONTEND.WPN_XO16_NAME


# class (object):
#     MDL_V1_1P = [[, b"\x"], [, b"\x"]]
#     MDL_V1_1P_HASH = ""
#     MDL_V1_1P_MATERIAL = ""
#     MDL_V1_1P_VANILLA = [[, b"\x"], [, b"\x"]]
#     MDL_VANILLA_1P_HASH = ""
#     MDL_VANILLA_1P_MATERIAL = ""
