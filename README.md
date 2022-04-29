[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Weather Alert App 

App to message me if the wind gust speed for tomorrow exceeds 30mph, so I can take down the basketball hoop!

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
