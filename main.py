from fastapi import FastAPI
import random
import google.generativeai as palm


app = FastAPI()


@app.get("/")
async def root():
    palm.configure(api_key="AIzaSyDIM7Ozafihl3KFtpj-35NlmqcCCDITfqM")
    models = [
        m
        for m in palm.list_models()
        if "generateText" in m.supported_generation_methods
    ]
    for m in models:
        # print(f"Model Name:{m.name}")
        return {"Model Name": m.name}

    # return {"message": "Hello World From Fast API", "data": 0}


@app.get("/random")
async def get_random():
    rn: int = random.randint(1, 100)
    return {"number": rn, "limit": 100}


@app.get("/random/{limit}")
async def get_random(limit: int):
    rn: int = random.randint(1, limit)
    return {"number": rn, "limit": limit}
