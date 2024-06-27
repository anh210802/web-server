FROM python:3.12.1-slim

# Install dependencies listed in requirements.txt
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Update package list and install sqlite3
RUN apt-get update && apt-get install -y sqlite3

# Copy the app into the container
COPY main.py /main.py

# Run the Streamlit app
CMD ["streamlit", "run", "/main.py", "--server.address=localhost"]

