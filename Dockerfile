FROM python:3.9.16-bullseye

RUN mkdir /xd
WORKDIR /xd
RUN chmod +777 /xd
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir static

RUN apt update; apt-get install -yy apache2

CMD ["bash","run.sh"]

EXPOSE 10000
