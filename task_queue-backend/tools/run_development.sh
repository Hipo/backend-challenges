#!/usr/bin/env bash

# This script starts the development environment using Docker
# Launch as: source tools/run_development.sh from the project's root

SERVICE_NAME="task_queue"

CONTAINER_UID=$(id -u) CONTAINER_GID=$(id -g) docker-compose stop
CONTAINER_UID=$(id -u) CONTAINER_GID=$(id -g) docker-compose rm --force
CONTAINER_UID=$(id -u) CONTAINER_GID=$(id -g) docker-compose up -d --remove-orphans --build
CONTAINER_UID=$(id -u) CONTAINER_GID=$(id -g) docker-compose exec ${SERVICE_NAME} bash
