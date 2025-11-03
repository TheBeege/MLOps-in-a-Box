FROM python:3.11-slim-bullseye AS release

ENV WORKSPACE_ROOT=/app/
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VERSION=1.8.3
ENV DEBIAN_FRONTEND=noninteractive
ENV POETRY_NO_INTERACTION=1
ENV ZENML_ENABLE_REPO_INIT_WARNINGS=False
ENV ZENML_CONFIG_PATH=/app/.zenconfig

# Install other system dependencies.
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends build-essential \
    gcc \
    python3-dev \
    build-essential \
    libglib2.0-dev \
    libnss3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create our user and workspace setup
RUN mkdir -p $WORKSPACE_ROOT && \
    groupadd -g 1000 pipeline_runner && \
    useradd pipeline_runner -u 1000 -g pipeline_runner -M -d $WORKSPACE_ROOT && \
    chown pipeline_runner:pipeline_runner $WORKSPACE_ROOT
# Make cache dir to avoid huggingface.transformers permissions issue
RUN mkdir /.cache && chown pipeline_runner:pipeline_runner /.cache
USER pipeline_runner
WORKDIR $WORKSPACE_ROOT


# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --link-mode=copy --compile-bytecode

ENV PYTHONPATH=/app/.venv/lib/python3.11/site-packages

# Copy the rest of the code.
COPY . $WORKSPACE_ROOT
