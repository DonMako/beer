# Use the official Python image as the base image
FROM python:3.8.10


ENV PYTHONUNBUFFERED 1
WORKDIR /beer
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","-u", "main.py"]
