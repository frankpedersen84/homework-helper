# Homework Helper and Tutor App

A Flask-based application that helps students with their homework through integration with Make.com.

## Features

- Webhook integration with Make.com
- Homework help request processing
- Grade-level specific responses
- Subject-based tutoring support

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your configuration:
```
PORT=5000
```

4. Run the application:
```bash
python app.py
```

## Webhook Integration

The application exposes a webhook endpoint at `/webhook` that accepts POST requests. The webhook expects the following JSON structure:

```json
{
    "question": "What is the pythagorean theorem?",
    "subject": "Mathematics",
    "grade_level": "8"
}
```

## Health Check

A health check endpoint is available at `/health` to monitor the application's status.

## Make.com Integration

To integrate with Make.com:
1. Deploy this application and note down the URL
2. In Make.com, create a new scenario
3. Add a webhook trigger and use the application's `/webhook` endpoint
4. Configure the webhook to send the required JSON structure
