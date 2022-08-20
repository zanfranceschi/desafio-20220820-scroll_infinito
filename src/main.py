import content
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="."), name="static")

templates = Jinja2Templates(directory=".")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def get(items: int = 10):
    return content.generate(items)


@app.get("/")
async def example(request: Request):
    return templates.TemplateResponse("desafio.html", {"request" : request})


@app.get("/example")
async def example(request: Request):
    return templates.TemplateResponse("example.html", {"request" : request})

