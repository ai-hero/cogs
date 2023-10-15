# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /agent
WORKDIR /agent

# Copy the current directory contents into the container at /app
COPY agent /agent

# Run the command to install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run hello.py when the container launches
CMD ["python", "entrypoint.sh"]
