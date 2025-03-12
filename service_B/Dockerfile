FROM python:3.9-slim

WORKDIR /app

COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "ser_b.py"]