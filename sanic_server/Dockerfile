FROM python:3.8-slim

ENV TZ=Europe/Moscow \
    TERM=xterm-color \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8

RUN apt-get update && apt-get install -y locales && \
    sed -i -e "s/# $LANG.*/$LANG UTF-8/" /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=$LANG

WORKDIR /app

RUN pip install pipenv
COPY Pipfile* /app/
RUN pipenv install --system --deploy --ignore-pipfile

COPY ./src /app/src
COPY start_server.sh /app
ENV PYTHON=python3 \
    PYTHONPATH=/app

EXPOSE 8080

CMD ["/app/start_server.sh"]
