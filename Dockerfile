From python:3.11-slim

WORKDIR /app

COPY app.py .
COPY data ./data 

VOLUME ["/app/data"]

CMD ["python", "app.py"]