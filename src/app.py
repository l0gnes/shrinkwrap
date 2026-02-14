from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root_ping() -> JSONResponse:
    return JSONResponse(
        {
            "ok" : True,
            "balls" : 200 # 200 balls?!?
        }
    )