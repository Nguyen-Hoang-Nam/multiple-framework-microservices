# FROM openjdk:11-jre-slim
FROM adoptopenjdk/openjdk11-openj9:jre-11.0.11_9_openj9-0.26.0-alpine
WORKDIR /
COPY wait-for-it.sh wait-for-it
RUN set -eux &&\
    apk --update add --no-cache bash coreutils &&\
    chmod +x wait-for-it
COPY target/spring-1.0.0.jar spring.jar
ENTRYPOINT ["./wait-for-it", "eureka:9000", "--", "java", "-jar", "spring.jar" ]
