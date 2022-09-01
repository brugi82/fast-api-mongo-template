from python:3.10.6

RUN curl -sSL https://install.python-poetry.org | python3 -

# install dependencies
COPY pyproject.toml poetry.lock ./code

RUN poetry install --no-interaction --no-ansi

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]