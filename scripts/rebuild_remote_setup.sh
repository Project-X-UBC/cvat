#!/bin/bash
docker-compose -f docker-compose.yml  -f docker-compose.override.yml build
docker-compose -f docker-compose.yml  -f docker-compose.override.yml up -d

# docker run --rm -d -p 8080:80 nginx 
