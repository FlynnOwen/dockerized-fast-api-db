# dockerized-fast-api-db
A small repo to test hosting a FastAPI API, connected to a database, both running in Docker containers.

## To view the app go to: http://3.25.173.58/ !

# Docs:
- https://docs.docker.com/compose/compose-file/ (compose)
- https://docs.docker.com/storage/volumes/ (database)
- https://docs.docker.com/samples/postgresql_service/ (database)
- https://testdriven.io/blog/fastapi-docker-traefik/
- https://docs.docker.com/compose/networking/ (Networking, connecting between containers)

Volumes show where in the Docker container data should be mounted. For example, maybe we would want to mount the postgres database at a particular place within the container.

# Front and Backend deployed together:
- https://wkrzywiec.medium.com/how-to-run-database-backend-and-frontend-in-a-single-click-with-docker-compose-4bcda66f6de

# AWS Deploy
- https://levelup.gitconnected.com/deploy-a-dockerized-fastapi-application-to-aws-cc757830ba1b
- https://www.cyberciti.biz/faq/how-to-install-docker-on-amazon-linux-2/
