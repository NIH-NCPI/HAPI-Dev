#!/bin/bash

LOCAL_PORT=8080
CONTAINER_NAME=hapi-fhir
CONFIG_FILENAME=app.yaml
DBDIR=db

# Create the database working directory and open the priveleges up
mkdir -p $DBDIR
chmod 777 $DBDIR

docker run \
    --rm \
    -p $LOCAL_PORT:8080 \
    -v $PWD/cfg:/configs \
    -v $PWD/$DBDIR:/hapi \
    -e "--spring.config.location=file:///configs/$CONFIG_FILENAME" \
    hapiproject/hapi:latest -n $CONTAINER_NAME
