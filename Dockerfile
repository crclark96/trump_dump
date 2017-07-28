FROM python:2
MAINTAINER Collin Clark <crclark96@gmail.com>

WORKDIR /usr/src/trump_dump

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY * ./

CMD ["python", "main.py"]