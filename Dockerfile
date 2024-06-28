FROM python:3.12.1-slim

# WORKDIR /app

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

RUN apt-get update && apt-get install -y sqlite3


COPY main.py /main.py

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=177.30.34.75"]

