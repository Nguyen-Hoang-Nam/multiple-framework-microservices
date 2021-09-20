from fastapi import FastAPI
from pydantic import BaseModel
import requests
import uvicorn
import py_eureka_client.eureka_client as eureka_client

app = FastAPI()

eureka_client.init(
    eureka_server="http://eureka:9000",
    app_name="fastapi",
    instance_port=8001,
)


class FastRequest(BaseModel):
    name: str


@app.post("/")
def hi(fast_request: FastRequest):
    return {"message": "FastAPI hi, " + fast_request.name}


@app.get("/hello/{framework}")
def hello(framework):
    url = eureka_client.walk_nodes(framework, "/", walker=lambda a: a)
    json = {"name": "FastAPI"}

    print(url)
    response = requests.post(url, json=json)
    data = response.json()
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
