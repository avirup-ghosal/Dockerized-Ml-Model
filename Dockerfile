FROM python:3.13.3-slim

WORKDIR /app

COPY requirements.txt .
COPY DTC.py .

RUN pip install -r requirements.txt

CMD ["python", "DTC.py"]
