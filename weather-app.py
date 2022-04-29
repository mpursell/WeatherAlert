from audioop import reverse
import requests
import os
from dotenv import load_dotenv, find_dotenv
from datetime import date, timedelta



def GetTomorrowFormattedDateAsString():

    today = date.today()
    tomorrow = today + timedelta(days=1)

    # adding a 'Z' to the end of the date to match the date format used from the API
    formattedDate = f"{tomorrow}Z"
    return str(formattedDate)

def GetWindGusts():

    load_dotenv(find_dotenv())
    apiKey = os.environ.get("API_KEY")

    nottinghamWeather = requests.get(f"http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/310015?res=3hourly&key={apiKey}")
    nottinghamWeatherJson = nottinghamWeather.json()

    periodList = nottinghamWeatherJson["SiteRep"]["DV"]["Location"]["Period"]

    tomorrow = GetTomorrowFormattedDateAsString()
    
    gustSpeedReports = []
    for period in periodList:
        if period["value"] == tomorrow:
            for report in period["Rep"]:
                # G here are the predicted wind gust speeds as string, so they
                # need to be cast to int for sorting / min-maxxing
                gustSpeedReports.append(int(report['G']))

    maxGustSpeed = max(gustSpeedReports)
    #print(maxGustSpeed)

    if maxGustSpeed > 30:
        return maxGustSpeed
    else:
        return 0

GetWindGusts()



