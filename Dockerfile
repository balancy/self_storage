FROM python:3.9.8-slim-buster

RUN mkdir /app

WORKDIR /app

COPY ./pyproject.toml .

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY ./entrypoint.sh .

ENTRYPOINT ["sh", "./entrypoint.sh"]