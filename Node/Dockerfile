FROM node:20
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY app.js .
ADD https://example.com/data.json .
EXPOSE 3000
ENTRYPOINT ["node"]
CMD ["app.js"]
