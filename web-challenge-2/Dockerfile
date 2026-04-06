FROM python:3.10-slim

WORKDIR /app

COPY app.py .
COPY files ./files

RUN pip install flask

EXPOSE 5000

CMD ["python3", "app.py"]