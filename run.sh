#!/bin/bash

docker build -t main-service -f ./services/main_service/Dockerfile ./services/main_service
docker build -t service-1 -f ./services/service_1/Dockerfile ./services/service_1
docker build -t service-2 -f ./services/service_2/Dockerfile ./services/service_2

docker-compose down
docker-compose up