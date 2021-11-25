FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3-pip python3-dev build-essential

WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]
CMD ["app.py"]

EXPOSE 5000
