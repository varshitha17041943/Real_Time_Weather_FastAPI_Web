from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests

app=FastAPI()
templates=Jinja2Templates(directory="templates")

@app.get("/")
def home(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="home.html"
    )

@app.post("/login")
def login(req:Request,username:str=Form(),password:str=Form()):
    return templates.TemplateResponse(
        request=req,
        name="location.html",
        )

@app.post("/weather_data",response_class=HTMLResponse)
def location(req:Request,location:str=Form()):
    query_params = {
    "key":"YOUR_WEATHER_API_KEY",
    "q":location,
    "aqi":"yes"
    }
    response = requests.get("https://api.weatherapi.com/v1/current.json",params=query_params)
    data = response.json()
    return templates.TemplateResponse(
        request=req,
        name="data.html",
        context={"weather_information":data}
    )
    