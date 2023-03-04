# Dockerfile

FROM python:3.9-slim-buster

# Set up working directory
WORKDIR /app

# Copy the Python script and requirements file
COPY requirements.txt .
COPY slack_notifier.py .
COPY main.py .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run when the container starts
CMD ["python", "main.py"]
