FROM node:17-slim

COPY package*.json .

RUN npm i

COPY . .

EXPOSE 300

CMD ["node","index"]