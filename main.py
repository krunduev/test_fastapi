from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    a: float
    b: float

app = FastAPI()

@app.post("/add")
def get_model(item:Item):
    return {"result": item.a + item.b}

@app.post("/sub")
def get_model(item:Item):
    return {"result": item.a - item.b}

@app.post("/mul")
def get_model(item:Item):
    return {"result": item.a * item.b}

@app.post("/div")
def get_model(item:Item):
    if item.b == 0:
        return {"error": "divider can't be 0"}
    else:
        return {"result": item.a / item.b}