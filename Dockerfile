# Stage 1: Use an official Python runtime as a parent image
# Using a 'slim' version keeps our final image smaller.
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the file with our dependencies into the container
COPY app/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of our application's code from the 'app' folder into the container
COPY app/ .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define the command to run our app. This is what starts when the container starts.
CMD ["python", "app.py"]