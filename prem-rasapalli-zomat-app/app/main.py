from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to prem-rasapalli-zomat 🍔"}

@app.get("/menu")
def menu():
    return ["pizza", "burger", "biryani"]
