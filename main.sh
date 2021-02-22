#!/bin/bash
docker-compose run --rm --service-ports app -c cd app; python3 main.py