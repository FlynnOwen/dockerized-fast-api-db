# dockerized-fast-api-db
A small repo to test hosting a FastAPI API, connected to a database, both running in Docker containers.

# Docs:
- https://docs.docker.com/compose/compose-file/ (compose)
- https://docs.docker.com/storage/volumes/ (database)
- https://docs.docker.com/samples/postgresql_service/ (database)
- https://testdriven.io/blog/fastapi-docker-traefik/

Volumes show where in the Docker container data should be mounted. For example, maybe we would want to mount the postgres database at a particular place within the container.