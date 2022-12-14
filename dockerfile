
FROM python:3.8.5-alpine3.12

WORKDIR /app

EXPOSE 5000

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "flask"]

CMD ["run", "-h", "0.0.0.0", "-p", "5000"]