from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI()
domain = "https://jsonplaceholder.typicode.com/"

class Post(BaseModel):
    title: str
    body: str
    userId: int
    id: int


@app.get("/")
async def root():
    return {"message": "My first FastAPI application"}


# # Get all posts
# @app.get("/posts")
# async def get_all_posts():
#     url = f"{domain}posts"

#     async with httpx.AsyncClient() as client:
#         response = await client.get(url)

#         if response.status_code != 200:
#             raise HTTPException(status_code=response.status_code, detail = "External API error")

#         return response.json()


# Get specific post
@app.get("/posts/{post_id}")
async def get_post_by_id(post_id: int):
    url = f"{domain}posts/{post_id}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail = "External API error")


        return response.json()


# Get posts of a user
@app.get("/posts", response_model=list[Post])
async def get_posts_by_user(user_id: int | None=None):
    url = f"{domain}posts"

    query_params = {}

    if user_id is not None:
        query_params["userId"] = user_id

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=query_params)

        return response.json()


# Add Post
@app.post("/posts", response_model=Post)
async def create_post(new_post: Post):
    url = f"{domain}posts"

    async with httpx.AsyncClient() as client:
        # response = await client.post(url, json=new_post.model_dump())

        return response.json()