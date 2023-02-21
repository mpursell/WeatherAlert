"""
App to check the wind gust speed for tomorrow
"""
import os
from datetime import date, timedelta

import requests
from dotenv import find_dotenv, load_dotenv
from twilio.rest import Client


class TwilioTextMessage:
    """
    class for Twilio text message
    """

    def __init__(self, message_text):
        load_dotenv(find_dotenv())
        self.account_sid = os.environ.get("TWILIO_account_sid")
        self.auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.twilio_phone_number = os.environ.get("TWILIO_PHONE_NUMBER")
        self.my_phone_number = os.environ.get("MY_PHONE_NUMBER")
        self.message_text = message_text
        self.twilio_client = Client(self.account_sid, self.auth_token)
        self.message = ""

    def send_message(self):
        """
        Method to send a text message
        """
        self.message = self.twilio_client.messages.create(
            to=self.my_phone_number,
            from_=self.twilio_phone_number,
            body=self.message_text,
        )


class ApiHandler:
    """
    Class to handle API calls
    """

    def __init__(self, url):
        load_dotenv(find_dotenv())
        self.url = url
        self.api_key = os.environ.get("API_KEY")

    def response(self) -> object:
        """
        Method to handle API Response
        """
        api_call = requests.get(f"{self.url}{self.api_key}", timeout=10)
        return api_call


def get_tomorrow_formatted_date_as_string() -> str:

    """
    Function to convert formatted date into a string
    """

    today = date.today()
    tomorrow = today + timedelta(days=1)

    # adding a 'Z' to the end of the date to match the date format used from the API
    formatted_date = f"{tomorrow}Z"
    return str(formatted_date)


def get_weather() -> object:

    """
    Function that calls API handler to get the forecast
    """

    weather_check = ApiHandler(
        "http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/310015?res=3hourly&key="
    )
    weather_json = weather_check.response().json()

    return weather_json


def get_wind_gusts() -> int:

    """
    function to parse the json and get the wind gust speed
    """
    nottinghamweather_json = get_weather()

    period_list = nottinghamweather_json["SiteRep"]["DV"]["Location"]["Period"]

    tomorrow = get_tomorrow_formatted_date_as_string()

    gust_speed_reports = []
    for period in period_list:
        if period["value"] == tomorrow:
            for report in period["Rep"]:
                # G here is the predicted wind gust speeds as string,
                # need to be cast to int for sorting / min-maxxing
                gust_speed_reports.append(int(report["G"]))

    max_gust_speed = max(gust_speed_reports)

    if max_gust_speed > 30:
        return max_gust_speed
    else:
        return 0


def check_weather() -> str:

    """
    function with logic to check the wind speed and trigger a message if above a threshold
    """

    if get_wind_gusts() >= 30:
        text_message = TwilioTextMessage(
            "Wind Over 30mph tomorrow.  Take down the Bball hoop!"
        )
        text_message.send_message()
        return "Wind Over 30mph tomorrow.  Take down the Bball hoop!"

    # else:
    #     text_message = TwilioTextMessage('No wind gusts')
    #     text_message.send_message()


check_weather()
