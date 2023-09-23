import os
from fastapi import FastAPI
import random
import requests

# import config
import google.generativeai as palm


app = FastAPI()


@app.get("/tp_traffic")
async def get_traffic():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/news.json"
    response = requests.get(url)
    data = response.json()
    return data
    # updateTime and News


"""     return {
        "data['News'][0]": data["News"][0],
        "Data Length": len(data["News"]),
        "updateTime": data["News"][0]["updateTime"],
        "chtmessage": data["News"][0]["chtmessage"],
    } """


@app.get("/palm")
async def get_palm():
    palm.configure(api_key=os.environ.get("api_key"))
    models = [
        m
        for m in palm.list_models()
        if "generateText" in m.supported_generation_methods
    ]
    # for m in models:
    # print(f"Model Name:{m.name}")
    # return {"Model Name": m.name}

    model = models[0].name
    # return {"Model Name": model}

    prompt = """
    Summarize this paragraph and detail some relevant context.
    Text: "I am by birth a Genevese, and my family is one of the most distinguished of that republic. My ancestors had been for many years"
    Summary: In this text, the narrator is describing his background and upbringing. He tells us that he is a native of Geneva, Switzerland.
    Text: "The thing the Time Traveller held in his hand was a glittering metallic framework, scarcely larger than a small clock, and very good"
    """

    completion = palm.generate_text(
        model=model, prompt=prompt, temperature=0.3, max_output_tokens=800
    )

    return {"completion result:": completion.result}


@app.get("/")
async def root():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/news.json"
    response = requests.get(url)
    data = response.json()
    # return data

    # updateTime and News
    for i in range(len(data["News"])):
        data["News"][i]["updateTime"] = data["News"][i]["updatetime"]
        data["News"][i]["chtmessage"] = data["News"][i]["chtmessage"]

    return {
        "data['News']": data["News"][i]["chtmesage"]
        + "-"
        + data["News"][i]["updateTime"]
    }
    # return {"message": "Hello World From Fast API", "data": 0}


@app.get("/random")
async def get_random():
    rn: int = random.randint(1, 100)
    return {"number": rn, "limit": 100}


@app.get("/random/{limit}")
async def get_random(limit: int):
    rn: int = random.randint(1, limit)
    return {"number": rn, "limit": limit}
