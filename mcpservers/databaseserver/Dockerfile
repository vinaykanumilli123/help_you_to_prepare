FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -r mcpservers/databaseserver/requirements.txt

EXPOSE 8003

CMD ["python", "-m", "mcpservers.databaseserver.server"]