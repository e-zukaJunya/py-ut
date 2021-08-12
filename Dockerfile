FROM python:3.8-slim
RUN apt-get update -y && apt-get upgrade -y && apt-get install git -y \
    && pip3 install pipenv
