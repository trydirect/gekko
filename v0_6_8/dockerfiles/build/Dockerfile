#FROM node:6-slim
FROM node:8.15.0-slim

RUN apt-get -qq update && apt-get install -y build-essential python curl git unzip
WORKDIR /var/www/html
RUN git clone git://github.com/askmike/gekko.git -b stable .
RUN npm install --only=production

EXPOSE 3000
