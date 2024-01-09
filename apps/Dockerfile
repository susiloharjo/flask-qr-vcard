# Use the official Python image as base
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install required packages
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5300 for Flask
EXPOSE 5300

# Command to run the application
CMD ["python", "app.py"]
