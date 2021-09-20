FROM python:3.9-alpine
WORKDIR /
COPY main.py main.py
COPY requirements.txt requirements.txt
COPY wait-for-it.sh wait-for-it
RUN pip install --no-cache-dir -r requirements.txt &&\
    set -eux &&\
    apk --update add --no-cache bash coreutils &&\
    chmod +x wait-for-it
ENTRYPOINT [ "./wait-for-it", "eureka:9000", "--", "python", "main.py" ]
