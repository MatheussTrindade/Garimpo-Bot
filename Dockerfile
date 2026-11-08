# Imagem enxuta, sem root, sem segredos embutidos.
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN useradd --create-home --uid 10001 garimpo
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app/ ./app/
RUN mkdir -p data config && chown -R garimpo:garimpo /app

USER garimpo

# Segredos entram em runtime: docker run --env-file .env ...
CMD ["python", "-m", "app"]
