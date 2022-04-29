import pytest
import requests
import os
from dotenv import load_dotenv, find_dotenv
from datetime import date, timedelta
from weather_app import *


def test_GetTomorrowFormattedDateAsString_format():

    # arrange
    tomorrow = "2022-04-30"

    # act
    tomorrowAsString = GetTomorrowFormattedDateAsString()

    # assert
    tomorrowAsString = "2022-04-30Z"


def test_GetTomorrowFormattedDateAsString_isString():

    # arrange
    tomorrow = "2022-04-30"

    # act
    tomorrowAsString = GetTomorrowFormattedDateAsString()

    # assert
    type(tomorrowAsString) == str


def test_GetWindGusts():

    # arrange
    nottinghamWeatherJson = {
        "SiteRep": {"Wx"},
        "DV": {
            "Location": {
                "Period": [
                    {
                        "type": "Day",
                        "value": "2022-04-29Z",
                        "Rep": [
                            {
                                "D": "NNE",
                                "F": "6",
                                "G": "29",
                                "H": "84",
                                "Pp": "9",
                                "S": "2",
                                "T": "6",
                                "V": "GO",
                                "W": "8",
                                "U": "1",
                                "$": "360",
                            }
                        ],
                    }
                ]
            }
        },
    }

    # act
    windGusts = GetWindGusts()

    # assert
    # if the wind gust is < 30, GetWindGusts should return 0, 
    # otherwise it should return the gust speed.
    windGusts == 0
    type(windGusts) == int
