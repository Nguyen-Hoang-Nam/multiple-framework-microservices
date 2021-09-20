# Multiple Framework Microservices

This is the Microservices' template for several web frameworks.

Currently, some services can not change such as discovery service (Eureka).

![Eureka](https://raw.githubusercontent.com/Nguyen-Hoang-Nam/readme-image/main/multiple-framework-microservices/eureka.jpg)

## Installation

```bash
docker-compose up -d
```

![Screenshot](https://raw.githubusercontent.com/Nguyen-Hoang-Nam/readme-image/main/multiple-framework-microservices/multiple-framework-microservices.jpg)

## Usage

You can send request between 2 services with this route
`http://localhost:<current-service-port>/hello/<other-service>`

![Route](https://raw.githubusercontent.com/Nguyen-Hoang-Nam/readme-image/main/multiple-framework-microservices/route.jpg)

## Services

### Eureka

This is the core service which other services must support

**hostname:** eureka

**port:** 9000

**route:**

- GET: localhost:9000

### Spring Boot

**hostname:** spring

**port:** 8000

**route:**

- GET: localhost:8000/hello/{other service}

**pros:**

- Work natively with Eureka, Zuul, etc
- Focus on business logic instead of configuration
- Rich microservices' documentation

**cons:**

- High memory usage
- Large docker image size

### FastAPI

**hostname:** fastapi

**port:** 8001

**route:**

- GET: localhost:8001/hello/{other service}

**pros:**

- Low memory usage (25 MB)
- Tiny docker image size
- Write less code to work with Eureka

**cons:**

- Hard to find microservice's documentation

### Gin

**hostname:** gin

**port:** 8002

**route:**

- GET: localhost:8002/hello/{other service}

**pros:**

- Use less dependencies
- Focus on business logic
- Rich microservices' documentation
- Extremely low memory (5 MB)

**cons:**

### Express.JS

**hostname:** express

**port:** 8003

**route:**

- GET: localhost:8003/hello/{other service}

**pros:**

- Lower memory usage than FastAPI (20 MB)
- Work natively with JSON
- Medium docker image size

**cons:**

- Not much microservices' documentation

## Contributing

Pull requests are welcome. For major changes,
please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
