#!/bin/bash

LOCAL_PORT=8080
CONTAINER_NAME=hapi-fhir
CONFIG_FILENAME=r4b.yaml
FHIR_VERSION=R4B
DBDIR=db


# Create the database working directory and open the priveleges up
mkdir -p $DBDIR
chmod 777 $DBDIR

# Right now, I can only get the R4B version to work (not counting 
# vanilla R4). So, just leave things as they are until the issues with R5 are
# worked out. 
echo docker run \
    --rm \
    -p $LOCAL_PORT:8080 \
    -v $PWD/cfg:/configs \
    -v $PWD/$DBDIR:/app/database \
    -e "--spring.config.location=file:///configs/$CONFIG_FILENAME" \
    hapiproject/hapi:latest -n $CONTAINER_NAME
