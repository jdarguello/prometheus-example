FROM python:3.13-slim as base

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir prometheus_client

# Copy application
COPY main.py .

# Use non-root user for security
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

USER appuser

EXPOSE 8000 8001

CMD ["python", "main.py"]