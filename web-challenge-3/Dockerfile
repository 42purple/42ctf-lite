FROM node:20-bullseye-slim

WORKDIR /app
COPY package*.json ./
RUN npm i

COPY . .
ENTRYPOINT ["node", "app.js"]
