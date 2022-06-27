FROM python:3.10.0-buster

RUN mkdir /app
COPY ./requirements.txt /app
COPY ./source /app
WORKDIR /app

RUN apt-get update && apt-get install git -y
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

ENTRYPOINT ["/usr/local/bin/python"]
CMD ["__main__.py"]
