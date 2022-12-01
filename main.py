from fastapi import FastAPI

app = FastAPI()

#Path operations "decorator"
@app.get("/")
def home():
    return {"hello": "World"}
