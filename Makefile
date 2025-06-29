train:
	docker build -f Dockerfile.train -t acme-ml-trainer:latest .
	docker run --rm -v $(PWD):/app acme-ml-trainer:latest