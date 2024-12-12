FROM python:3.13-alpine

WORKDIR /app

COPY app.py /app/

RUN pip install flask pymysql cryptography flask_cors logging

ENV POART=6000
ENV DB_HOST=host.docker.internal
ENV DB_USER=root
ENV DB_PASSWORD=root
ENV DB_NAME=devops

EXPOSE $POART

CMD ["python", "app.py"]
