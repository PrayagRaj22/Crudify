# ---------- Stage 1: Builder ----------
FROM python:3.11-slim AS builder

WORKDIR /install

COPY requirements.txt .

RUN pip install --prefix=/install/deps --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y curl

# ---------- Stage 2: Runtime ----------

FROM python:3.11-slim

WORKDIR /app

# ---------- Copy installed dependencies from builder ----------

COPY --from=builder /install/deps /usr/local

# ---------- Copy application code ----------
COPY src/ /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]