FROM golang:1.22-alpine

ENV LOCAL_ONLY=TRUE
ENV PORT=8080
ENV FUNCTION_TARGET=dec-parana

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN go build -o /start ./cmd/main.go

EXPOSE 8080

CMD ["/start"]
