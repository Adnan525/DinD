FROM python:3.9-slim

WORKDIR /app

# Install Docker CLI
RUN apt-get update && \
    apt-get install -y docker.io && \
    apt install -y vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy everything from the current directory
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "ser_a.py"]