# This Dockerfile is a copy of sicnpcf-infra/docker/Dockerfile.backend
# Keep in sync. Source of truth: sicnpcf-infra.
# syntax=docker/dockerfile:1.7
ARG PYTHON_VERSION=3.12-slim-bookworm

FROM python:${PYTHON_VERSION} AS base
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

FROM base AS deps-prod
COPY requirements/base.txt requirements/prod.txt /tmp/req/
RUN pip install -r /tmp/req/prod.txt

FROM base AS deps-dev
COPY requirements/base.txt requirements/dev.txt /tmp/req/
RUN pip install -r /tmp/req/dev.txt

FROM deps-prod AS prod
COPY . /app
RUN python manage.py collectstatic --noinput || true
USER 1000
EXPOSE 8000
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--access-logfile", "-"]

FROM deps-dev AS dev
COPY . /app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
