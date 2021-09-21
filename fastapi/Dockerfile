FROM python:3.9-alpine
WORKDIR /
COPY wait-for wait-for
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py main.py
ENTRYPOINT [ "./wait-for", "eureka:9000", "--", "python", "main.py" ]
