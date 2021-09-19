from fastapi import FastAPI, requests
from pydantic import BaseModel
import requests
import uvicorn

app = FastAPI()


class FastRequest(BaseModel):
    name: str


@app.post("/")
def hi(fast_request: FastRequest):
    return {"message": "Python hi, " + fast_request.name}


@app.get("/hello/{framework}")
def hello(framework):
    url = "localhost:8000"
    data = {"name": "FastAPI"}

    response = requests.post(url, data)
    json = response.json()
    return json.message


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
