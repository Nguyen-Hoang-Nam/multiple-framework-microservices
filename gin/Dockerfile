FROM golang:1.16.8-alpine3.14
WORKDIR /app
ENV GIN_MODE=release
COPY wait-for-it.sh wait-for-it
RUN set -eux &&\
    apk --update add --no-cache bash coreutils &&\
    chmod +x wait-for-it
COPY go.mod ./
COPY go.sum ./
RUN go mod download
COPY . ./
RUN go build -o /gin
ENTRYPOINT [ "./wait-for-it", "eureka:9000", "--", "/gin"]
