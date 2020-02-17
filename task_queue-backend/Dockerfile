FROM python:3.8.1 as base

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get -y --no-install-recommends install \
    gdal-bin \
    && apt-get install -y --no-install-recommends postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY . .
RUN pip install -U pip && pip install -r requirements.txt

WORKDIR /task_queue

FROM base as application
COPY . .
