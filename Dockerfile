FROM python:3.10-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y curl gcc libmariadb-dev
RUN pip install --upgrade pip
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.5.0 python -

ENV PATH=${POETRY_HOME}/bin:${PATH}
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock README.md ./
COPY ./q_q ./q_q
RUN poetry install

CMD ["poetry", "run", "uvicorn", "--host", "0.0.0.0","q_q.main:app"]
