#!/bin/sh

# ATTENTION, CETTE INSTRUCTION VA STOPPER TOUS LES CONTAINERS
# sudo docker kill $(sudo docker ps -q)

#cd ../..
docker-compose up -d
docker-compose exec work-env python src/pyspark/main.py
