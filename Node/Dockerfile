FROM node:20
WORKDIR /app
RUN apt-get update
COPY app.js .
EXPOSE 3000
ENTRYPOINT ["node"]
CMD ["app.js"]
