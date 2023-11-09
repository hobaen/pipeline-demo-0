# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install pytest for running unit tests and pylint for linting
RUN pip install pytest pylint

# Command to run the application
CMD ["python", "stats_program.py"]