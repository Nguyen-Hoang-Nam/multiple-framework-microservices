FROM node:16-alpine3.14
WORKDIR /app
ENV NODE_ENV=production
COPY wait-for-it.sh wait-for-it
RUN set -eux &&\
    apk --update add --no-cache bash coreutils &&\
    chmod +x wait-for-it
COPY ["package.json", "package-lock.json*", "./"]
RUN npm install --production
COPY . .
ENTRYPOINT [ "./wait-for-it", "eureka:9000", "--", "node", "app.js" ]
