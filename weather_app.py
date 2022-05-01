from itsdangerous import json
import requests
import os
from dotenv import load_dotenv, find_dotenv
from datetime import date, timedelta
from twilio.rest import Client

class TwilioTextMessage:
    
    def __init__(self, messageText):
        load_dotenv(find_dotenv())
        self.accountSID = os.environ.get('TWILIO_ACCOUNT_SID')
        self.authToken = os.environ.get('TWILIO_AUTH_TOKEN')
        self.twilioPhoneNumber = os.environ.get('TWILIO_PHONE_NUMBER')
        self.myPhoneNumber = os.environ.get('MY_PHONE_NUMBER')
        self.messageText = messageText

    def send_message(self):
        self.twilioClient = Client(self.accountSID, self.authToken)

        self.message = self.twilioClient.messages.create(
            to=self.myPhoneNumber,
            from_=self.twilioPhoneNumber,
            body=self.messageText
        )

class ApiHandler:
    
    def __init__(self, url):
        load_dotenv(find_dotenv())
        self.url = url
        self.apiKey = os.environ.get("API_KEY")
    
    def response(self):
        apiCall = requests.get(f"{self.url}{self.apiKey}")
        return apiCall



def GetTomorrowFormattedDateAsString():

    today = date.today()
    tomorrow = today + timedelta(days=1)

    # adding a 'Z' to the end of the date to match the date format used from the API
    formattedDate = f"{tomorrow}Z"
    return str(formattedDate)

def GetWeather():

    weatherCheck = ApiHandler("http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/310015?res=3hourly&key=")
    weatherJson = weatherCheck.response().json()

    return weatherJson
    
def GetWindGusts():

    # load_dotenv(find_dotenv())
    # apiKey = os.environ.get("API_KEY")

    # nottinghamWeather = requests.get(
    #     f"http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/310015?res=3hourly&key={apiKey}"
    # )
    nottinghamWeatherJson = GetWeather()

    periodList = nottinghamWeatherJson["SiteRep"]["DV"]["Location"]["Period"]

    tomorrow = GetTomorrowFormattedDateAsString()

    gustSpeedReports = []
    for period in periodList:
        if period["value"] == tomorrow:
            for report in period["Rep"]:
                # G here is the predicted wind gust speeds as string,
                # need to be cast to int for sorting / min-maxxing
                gustSpeedReports.append(int(report["G"]))

    maxGustSpeed = max(gustSpeedReports)

    if maxGustSpeed > 30:
        return maxGustSpeed
    else:
        return 0


def checkWeather():

    if GetWindGusts() >= 30:
        textMessage = TwilioTextMessage('Wind Over 30mph tomorrow.  Take down the Bball hoop!')
        textMessage.send_message()
    else:
        textMessage = TwilioTextMessage('No wind gusts')
        textMessage.send_message()


checkWeather()


