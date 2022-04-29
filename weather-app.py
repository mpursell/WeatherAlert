import requests
import os
from dotenv import load_dotenv, find_dotenv



load_dotenv(find_dotenv())

apiKey = os.environ.get("API_KEY")

def GetWeather():
    nottinghamWeather = requests.get(f"http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/310015?res=3hourly&key={apiKey}")
    
    nottinghamWeatherJson = nottinghamWeather.json()

    print(nottinghamWeatherJson["SiteRep"]["DV"]["Location"]["Period"])

GetWeather()


