from fastapi import FastAPI
from pydantic import BaseModel
from urllib import request

import uvicorn
import py_eureka_client.eureka_client as eureka_client
import json

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

    data = {"name": "FastAPI"}
    data = str(json.dumps(data)).encode("utf-8")

    req = request.Request(url, data)  # type: ignore

    response = request.urlopen(req)
    return json.loads(response.read())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)  # type: ignore
