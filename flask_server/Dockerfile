FROM python:3.6-alpine3.7

ENV TZ Europe/Moscow
ENV TERM xterm
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY requirements.txt /
RUN pip3 install --no-cache-dir -r /requirements.txt

COPY . /app
WORKDIR /app
ENV PYTHON python3
ENV PYTHONPATH /app

EXPOSE 8080

ENV UWSGI_THREADS 10

CMD ["uwsgi", "./uwsgi.ini"]
