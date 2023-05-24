FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH='/'

COPY ./poetry.lock /
COPY ./pyproject.toml /

RUN apt-get update -y && apt-get install curl -y \
&& curl -sSL https://install.python-poetry.org | python3 - \
&& poetry config virtualenvs.create false \
&& poetry install \
&& apt-get remove curl -y

RUN addgroup --system app && adduser --system --group app

USER app

COPY ./app /app
WORKDIR /app