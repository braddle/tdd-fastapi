test: docker_build_test
	docker-compose down
	docker-compose up -d
	docker-compose exec -T http poetry run pytest
	docker-compose down

run: docker_build_test
	docker-compose up

docker_build_test:
	docker build . -t service_test