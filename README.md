# HAPI-Dev
This repository provides a simple helper to launch a local FHIR server that persists using local storage and has some pre-defined defaults built in. 

At this time, it is set to use the H2 database, which is the easiest to set up but if performance turns out to be undesirable, it may get updated to use Postgres. 

# R4/R4B Support
At this time, we have two configurations ready for use as dev environments: R4 and R4B 

R5 results in errors that aren't obvious to me what is failing, so, until I have more time to dig into the issue, R5 support is up to you to work out. 

# Usage
The script itself, start-server.py, should run out of the box with Python 3.8 or later. 

By default, the following command will bring a local FHIR server running R4B up. 

> ./start-server.py 

This will bring the server up using R4B and is based on the configuration settings found inside ''cfg/R4B/app.yaml''. This configuration also specifies that data will persist in an h2 database inside a directory mapped from the local directory, ''db''. The R4 and R4B databases are not compatible, so each version has a different file specified for that DB. 

## Port
By default, the port setting is 8080, however the user can specify whichever port they want using the ''-p'' flag. 

## detach
By default, the application runs in the foreground of the shell in which it was started. If you wish to send the process to the background, you can use the flag -d, --detach when run. This will launch docker in detached mode. The container ID will be reported immediately which you can use to reattach and stop (via docker commands).

## help
For a complete list of commands, please see the standard linux help listing using the flag ''-h''. 
