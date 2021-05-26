# TPL - Third Party Libraries
import uvicorn
from fastapi import FastAPI
# LPL - Local Python Libraries
from lib.core.enums import API


def apiServer():
    app = FastAPI()

    @app.get("/weapon")
    def weaponsInfo():
        return("Baguette")

    # TODO find a better way to do this
    # XXX JS py-shell library ?
    # XXX Or JS using a uvicorn command by itself ? Is that even doable ?
    if __name__ == "lib.core.api":
        uvicorn.run(app, port=API.SERVER_PORT)
