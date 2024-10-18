# Use official Python image
FROM python:3.9

# Set working directory in container
WORKDIR /app

# Copy current directory contents into container
COPY ./app /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port the Flask app runs on
EXPOSE 5000

# Define environment variable for Flask app
ENV FLASK_APP=app.py

# Run Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
