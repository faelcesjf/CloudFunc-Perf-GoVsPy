FROM golang:1.22-alpine

ENV LOCAL_ONLY=TRUE
ENV PORT=8080

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN go build -o /docker-gs-ping ./cmd/main.go

EXPOSE 8080

CMD ["/docker-gs-ping"]
