FROM python:3.11-alpine3.18
WORKDIR /app
COPY requirement.txt .
RUN pip install --no-cache-dir --upgrade -r requirement.txt
COPY . .