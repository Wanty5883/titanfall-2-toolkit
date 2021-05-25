# SPL - Standard Python Libraries
import sys
# TPL - Third Party Libraries
from flask import Flask
from flask import request
from flask_restful import Api
from flask_restful import reqparse
from flask_restful import Resource
# LPL - Local Python Libraries
from lib.core.attr import attr_wpnList
from lib.core.enums import API
from lib.core.log import logger
from lib.r2.wpn import wpn_hashMDL
from lib.r2.wpn import wpn_convertMDL
import lib.r2.wpn_enums as ENUMS_WPN


def apiServer():
    # global app  # Might not be used
    app = Flask(API.SERVER_NAME)
    api = Api(app)

    api.add_resource(WeaponInfo, "/weapon/<string:weaponName>")
    api.add_resource(WeaponModding, "/weapon")

    app.run(host="localhost", port=API.SERVER_PORT, debug=True)

    # TODO doesn't work, would be nice to find another way
    @app.route("/shutdown", methods=["POST"])
    def serverShutdown():
        shutdown = request.environ.get("{0}.server.shutdown".format(API.SERVER_NAME))
        if shutdown is None:
            raise RuntimeError("The server {0} is not running".format(API.SERVER_NAME))
        else:
            shutdown()


class WeaponInfo(Resource):
    def get(self, weaponName):
        wpn_enums = attr_wpnList()
        for x in wpn_enums:
            if weaponName == getattr(getattr(ENUMS_WPN, x), "WPN_NAME_SHORT"):
                r = {
                    "name": getattr(getattr(ENUMS_WPN, x), "WPN_NAME"),
                    "nameshort": getattr(getattr(ENUMS_WPN, x), "WPN_NAME_SHORT"),
                    "desc": getattr(getattr(ENUMS_WPN, x), "WPN_DESC"),
                    "longdesc": getattr(getattr(ENUMS_WPN, x), "WPN_LONGDESC"),
                    "attribute": x
                }
                return(r)


def wpnArgsMods():
    args = reqparse.RequestParser()
    # Mandaroty arguments
    args.add_argument("rootDirectory", type=str, help="Set the extracted VPK directory", required=True)
    # Function arguments
    args.add_argument("wpnConvertMDL", type=bool, help="Convert a weapon mdl to a defined version")
    args.add_argument("wpnHashMDL", type=bool, help="Hash a weapon model file")
    # General arguments
    args.add_argument("wpnFileType", type=str, help="Choose the 3D model file type (1P, 3P, etc.)")
    args.add_argument("wpnFileVersion", type=str, help="Choose the 3D model file version")
    args.add_argument("wpnFileTarget", type=str, help="Choose the 3D model target file")
    args.add_argument("wpnStructTarget", type=str, help="Choose the 3D model struct target")
    return(args.parse_args())


class WeaponModding(Resource):
    def get(self):
        pass

    def post(self):
        args = wpnArgsMods()

        if not args["wpnFileTarget"] in attr_wpnList():
            logger.critical("wpnFileTarget is not correct")
            sys.exit(0)
        if not args["wpnStructTarget"] in attr_wpnList():
            logger.critical("wpnStructTarget is not correct")
            sys.exit(0)
        if args["wpnConvertMDL"]:
            if not args["wpnFileType"]:
                logger.critical("")
                sys.exit(0)
            if not args["wpnFileVersion"]:
                logger.critical("")
                sys.exit(0)
            if not args["wpnFileTarget"]:
                logger.critical("")
                sys.exit(0)
            if not args["wpnStructTarget"]:
                logger.critical("")
                sys.exit(0)
            wpn_convertMDL(
                args["rootDirectory"],
                args["wpnFileType"],
                args["wpnFileVersion"],
                args["wpnFileTarget"],
                args["wpnStructTarget"]
            )
            return("ok")
        return({"data": args})
