from fastapi import FastAPI
from fastapi.responses import HTMLResponse
#app object will be used to define all our routes.
app = FastAPI()

#Data for Testing Purpose
posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

#Starter API endpoint: Home Route("/")
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def hello():
    return f"<h1>{posts[0]['title']}</h1>"

#API endpoint to view the data from the List[posts]
@app.get("/view")
def view_data():
    return posts

