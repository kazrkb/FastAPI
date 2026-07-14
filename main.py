from fastapi import FastAPI, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts = [
    {
        "id": 1,
        "title": "First Post",
        "content": "This is the first post.",
        "author": "John Doe",
        "date_posted": "July 5, 2026",
    },
    {
        "id": 2,
        "title": "Second Post",
        "content": "This is the second post.",
        "author": "Jane Smith",
        "date_posted": "July 4, 2026",
    },
    {
        "id": 3,
        "title": "Third Post",
        "content": "This is the third post.",
        "author": "Corey Schafer",
        "date_posted": "July 3, 2026",
    },
]


@app.get("/", include_in_schema=False, name='home')
@app.get("/posts", include_in_schema=False, name='posts')
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})


@app.get("/post/{post_id}", include_in_schema=False, name="post_page")
def post_page(request: Request, post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return templates.TemplateResponse(
                request,
                "post.html",
                {"post": post, "title": post["title"]}
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Post was not found"
    )


@app.get("/api/posts")
def get_posts():
    return posts

@app.get("/api/posts/{post_id}")
def get_post(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post was not found")