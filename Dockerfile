# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install any dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . /app/

# Expose the port your app will run on (if applicable, replace with correct port)
EXPOSE 8000

# Command to run your application (adjust according to your app's entry point)
CMD ["python", "src/agents/rag/rag_app.py"]
