FROM python:3.9.5-slim

WORKDIR c-api

COPY . /c-api

RUN pip install -r requirements.txt

EXPOSE 5000

CMD uvicorn main:app --host "0.0.0.0" --port "5000"


#FROM ubuntu
#
#WORKDIR c-api
#
#COPY . /c-api
#
#RUN apt update && apt upgrade
#RUN apt install python3 -y && apt install python3-pip -y
#RUN pip3 install -r requirements.txt
#
#EXPOSE 5000
#
#CMD uvicorn main:app --host "0.0.0.0" --port "5000"