FROM python:3.9-slim-buster

# Set up working directory
WORKDIR /app

COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run when the container starts
CMD ["python", "main.py"]
