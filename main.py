from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes import cv, job_match
import uvicorn
from middleware import CustomMiddleware

app = FastAPI()


templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(CustomMiddleware)
app.include_router(cv.router)
app.include_router(job_match.router)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)



# agregarle requisitos del puesto y luego yo subir mi CV y que el me diga mi score para ese puesto

