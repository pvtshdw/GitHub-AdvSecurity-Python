FROM python:3
MAINTAINER Brian Outlaw "brian.outlaw@kasasa.com"

# Update the image
RUN apt-get update -y

#COPY . /app
RUN mkdir /cmtrainer
WORKDIR /cmtrainer
ADD requirements.txt /cmtrainer/
RUN pip3 install -r requirements.txt
ADD . /cmtrainer/

ENTRYPOINT ["python3", "-u"]
CMD ["app.py"]
