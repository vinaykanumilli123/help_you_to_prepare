FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r mcpservers/storageserver/requirements.txt

EXPOSE 8001

CMD ["uvicorn", "mcpservers.storageserver.server:app", "--host", "0.0.0.0", "--port", "8001"]