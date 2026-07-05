from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts = [
    {
        "id": 1,
        "title": "First Post",
        "content": "This is the first post.",
        "author": "Rakib",
        "date_posted": "July 5, 2026",
    },
    {
        "id": 2,
        "title": "Second Post",
        "content": "This is the second post.",
        "author": "Rakib",
        "date_posted": "July 4, 2026",
    },
    {
        "id": 3,
        "title": "Third Post",
        "content": "This is the third post.",
        "author": "Rakib",
        "date_posted": "July 3, 2026",
    },
]


@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})


@app.get("/api/posts")
def get_posts():
    return posts
