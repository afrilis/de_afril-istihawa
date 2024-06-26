FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r /app/requirements.txt
RUN pip install --no-cache /wheels/*

ENV CSV_FILE=data.csv

CMD ["python", "main.py"]
