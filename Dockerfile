FROM python:3.8.2

ENV PYTHONBUFFERED True
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN apt-get update
RUN apt-get install default-jdk -y

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app