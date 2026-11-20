from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()
domain = "https://jsonplaceholder.typicode.com/"

@app.get("/")
async def root():
    return {"message": "My first FastAPI application"}


# Get all posts
@app.get("/posts")
async def get_all_posts():
    url = f"{domain}posts"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail = "External API error")

        return response.json()


# Get specific post
@app.get("/posts/{post_id}")
async def get_post_by_id(post_id: int):
    url = f"{domain}posts/{post_id}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail = "External API error")


        return response.json()