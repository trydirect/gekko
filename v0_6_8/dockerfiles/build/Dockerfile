FROM node:8.16.0-slim

RUN apt-get -qq update && apt-get install -y  --no-install-recommends build-essential python curl git unzip supervisor \
 && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /var/www/html
RUN git clone git://github.com/askmike/gekko.git -b stable .
RUN npm install --only=production
RUN groupadd -r -g 2000 gekko; useradd -r -u 2000 -g 2000 -m -c "app account" -d /home/gekko -s /bin/bash gekko
RUN chown -R gekko. /var/log/supervisor && \
    chown -R gekko. /var/run
USER gekko
EXPOSE 3000
