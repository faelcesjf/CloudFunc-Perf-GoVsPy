package main

import (
	"log"
	"os"

	"github.com/GoogleCloudPlatform/functions-framework-go/funcframework"
	_ "veri.com/dec-parana"
)

func main() {
	port := "8080"
	if envPort := os.Getenv("PORT"); envPort != "" {
		port = envPort
	}

	hostname := "0.0.0.0"
	if localOnly := os.Getenv("LOCAL_ONLY"); localOnly == "true" {
		hostname = "127.0.0.1"
	}
	if err := funcframework.StartHostPort(hostname, port); err != nil {
		log.Fatalf("funcframework.StartHostPort: %v\n", err)
	}
}
