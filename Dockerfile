FROM python:3.8

WORKDIR /code

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/
EXPOSE 8000

