FROM python:3.9.2-alpine3.13
RUN apk update && apk upgrade && apk add bash curl gcc musl-dev
COPY . ./app
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
RUN cd app && source $HOME/.poetry/env && poetry config virtualenvs.create false && poetry update && poetry install
CMD ["python3", "app/wargaming_test/app.py"]