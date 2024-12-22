FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Explicitly set the port for App Runner
ENV PORT=8080
EXPOSE 8080

CMD ["python", "app.py"]
