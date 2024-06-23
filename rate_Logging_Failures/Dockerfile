FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Ensure logs directory exists
RUN mkdir logs

# Initialize logs before running the application
RUN python init_logs.py

CMD ["python", "app.py"]
