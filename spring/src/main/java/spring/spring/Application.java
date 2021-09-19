package spring.spring;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;
import spring.spring.request.SpringRequest;
import spring.spring.response.SpringResponse;

@SpringBootApplication
@RestController
public class Application {

    private WebClient webClient;

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }

    @PostMapping
    public SpringResponse hi(@RequestBody SpringRequest language) {
        String message = "Java hi, " + language.getName();

        return new SpringResponse(message);
    }

    @GetMapping(path = "/hello/{language}")
    public String hello(@PathVariable String language) {
        SpringRequest springRequest = new SpringRequest(language);

        SpringResponse springResponse = new SpringResponse();

        webClient
            .post()
            .uri("localhost:8001/hello")
            .body(Mono.just(springRequest), SpringRequest.class)
            .retrieve()
            .bodyToMono(SpringResponse.class)
            .subscribe(
                result -> springResponse.setMessage(result.getMessage())
            );

        return springResponse.getMessage();
    }
}
