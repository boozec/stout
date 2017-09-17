FROM alpine:3.4
RUN apk add --update \
	python3
COPY . /app
WORKDIR /app
CMD ["python3", "lib/app.py"]
