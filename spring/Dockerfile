FROM openjdk:11-jre-slim
WORKDIR /
COPY target/spring-1.0.0.jar spring.jar
COPY wait-for-it.sh wait-for-it.sh
ENTRYPOINT ["./wait-for-it.sh", "eureka:9000", "--", "java", "-jar", "spring.jar" ]
