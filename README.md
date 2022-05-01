[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Weather Alert App 

App to message me if the wind gust speed for tomorrow exceeds 30mph, so I can take down the basketball hoop!

## Pre-requisites

You'll need:

* An API account with the Met Office - https://www.metoffice.gov.uk/services/data/datapoint/api
* A Twilio API account - https://console.twilio.com/
* A .env file creating with the following:
    * API_KEY (this is your Met Office API key)
    * TWILIO_ACCOUNT_SID
    * TWILIO_AUTH_TOKEN
    * TWILIO_PHONE_NUMBER
    * MY_PHONE_NUMBER (your personal phone number)
    
All the TWILIO requirements can be found in the Twilio console once you're signed in

## Virtual Environment

Developed and tested in venv.  

* Create a new venv with 

```bash
venv <folder name>
```
* Pull the code down into the folder
* Activate the virtual env with 
```bash
source bin/activate
```
* Install the project requirements with 
```bash
pip install -r requirements.txt
```


## Testing

From inside the virtual environment, run

```bash
python3 -m pytest -v tests
```
from the application root folder.
