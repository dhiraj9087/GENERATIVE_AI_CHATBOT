# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the app runs on
EXPOSE 8000

# Define environment variable
ENV COHERE_API_KEY='xtXzFR7Yzyb3T9vuCQ563oMdRLXm000eQiDgObuv'

# Run the application
CMD ["python", "app.py"]
