#!/bin/bash

docker build -t flask-main -f ./main/Dockerfile ./main
docker build -t flask-auth -f ./auth/Dockerfile ./auth
docker build -t flask-booking -f ./booking/Dockerfile ./booking

docker-compose up