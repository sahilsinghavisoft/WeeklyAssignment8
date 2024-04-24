FROM python:3.11

WORKDIR /weeklyassignment8

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -

ENV PATH="/etc/poetry/bin:$PATH"

COPY ../poetry.lock /weeklyassignment8//
COPY ../pyproject.toml /weeklyassignment8
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-ansi 
COPY .. .


CMD ["uvicorn", "ml_deployment.classification_application:app", "--host", "0.0.0.0", "--port", "8000"]

