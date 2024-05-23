
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/health")
def health():
    return {"status": "UP"}


@app.get("/")
def home(request: Request):

    context = {
        "request": request,
        "title": "Hello World!"
    }

    return templates.TemplateResponse("index.html", context)


app.mount("/", StaticFiles(directory="htdocs", html=True))
