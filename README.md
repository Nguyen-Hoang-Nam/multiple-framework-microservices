# Multiple Framework Microservices

Bootstrap Microservices' template for several web frameworks.

Currently, some services can not be replaced such as discovery service (Eureka).

![Eureka](https://raw.githubusercontent.com/Nguyen-Hoang-Nam/readme-image/main/multiple-framework-microservices/eureka.jpg)

## Installation

```bash
docker-compose up -d
```

![Screenshot](https://raw.githubusercontent.com/Nguyen-Hoang-Nam/readme-image/main/multiple-framework-microservices/multiple-framework-microservices.jpg)

## Usage

You can send a request between 2 services with this route
`http://localhost:9001/{hostname}/hello/{other hostname}`

![Route](https://raw.githubusercontent.com/Nguyen-Hoang-Nam/readme-image/main/multiple-framework-microservices/route.jpg)

## Services

| Hostname | Port | Route                                                 |
| -------- | ---- | ----------------------------------------------------- |
| eureka   | 9000 | GET: localhost:9000                                   |
| gateway  | 9001 | GET: localhost:9001/{hostname}/hello/{other hostname} |
| spring   | 8000 | GET: localhost:8000/hello/{other hostname}            |
| fastapi  | 8001 | GET: localhost:8001/hello/{other hostname}            |
| gin      | 8002 | GET: localhost:8002/hello/{other hostname}            |
| express  | 8003 | GET: localhost:8003/hello/{other hostname}            |

## Eureka

This is the core service which other services must support

## Spring Cloud Gateway

**pros:**

- Better configuration than Zuul
- More portable

**cons:**

- Less documentation about working with Spring Netflix

## Spring Boot

**pros:**

- Work natively with Eureka, Zuul, etc
- Focus on business logic instead of configuration
- Rich microservices' documentation

**cons:**

- High memory usage
- Large docker image size

## FastAPI

**pros:**

- Low memory usage (25 MB)
- Tiny docker image size
- Write less code to work with Eureka

**cons:**

- Hard to find microservice's documentation

## Gin

**pros:**

- Use less dependencies
- Focus on business logic
- Rich microservices' documentation
- Extremely low memory (5 MB)
- Extremely low docker image size (multiple build stage 13 MB)

**cons:**

## Express

**pros:**

- Lower memory usage than FastAPI (20 MB)
- Work natively with JSON
- Medium docker image size

**cons:**

- Not much microservices' documentations

## Contributing

Pull requests are welcome. For major changes,
please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
