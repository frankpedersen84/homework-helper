FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Explicitly set the port for App Runner
ENV PORT=8080
EXPOSE 8080

# Use Gunicorn instead of Flask's development server
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
