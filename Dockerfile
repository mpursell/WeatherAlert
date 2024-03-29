FROM python:3.9-slim-buster as base

RUN mkdir -p /usr/src/weather_alert

WORKDIR /usr/src/weather_alert

RUN apt update -y &&\ 
    apt install curl -y

COPY . /usr/src/weather_alert/

RUN pip install -r /usr/src/weather_alert/requirements.txt &&\
    chmod +x ./docker-entrypoint.sh &&\
    chmod +x ./docker-entrypoint-test.sh 

FROM base as local

# run app via a shell script 
CMD ["./docker-entrypoint.sh"]

FROM base as test

CMD ["./docker-entrypoint-test.sh"]