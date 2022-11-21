# syntax=docker/dockerfile:1
FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get -y install gcc
RUN pip install -Ur requirements.txt
CMD ["python3","./main.py"]