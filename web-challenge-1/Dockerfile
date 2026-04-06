FROM node:latest

RUN apt update && apt install -y nginx

WORKDIR /app
COPY package*.json ./
RUN npm i
COPY . .
RUN chown -R node:node /app

COPY ./nginx.conf /etc/nginx/nginx.conf
RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]