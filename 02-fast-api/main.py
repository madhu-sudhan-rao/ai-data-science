from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()
domain = "https://jsonplaceholder.typicode.com/"

@app.get("/")
async def root():
    return {"message": "My first FastAPI application"}


