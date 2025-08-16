FROM python:3.11-slim

WORKDIR /app

RUN apt-get update

COPY app.py .

EXPOSE  3000

CMD ["app.py"]
