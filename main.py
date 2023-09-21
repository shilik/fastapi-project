from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World From Fast API", "data": 0}


@app.get("/random")
async def get_random():
    rn: int = random.randint(1, 100)
    return {"number": rn, "limit": 100}
