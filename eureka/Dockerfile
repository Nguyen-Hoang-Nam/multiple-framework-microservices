FROM openjdk:11-jre-slim
WORKDIR /
COPY target/eureka-1.0.0.jar eureka.jar
ENTRYPOINT [ "java", "-jar", "eureka.jar" ]
