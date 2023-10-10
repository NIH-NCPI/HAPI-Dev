# HAPI-Dev
This repository provides some simple helper scripts to launch a local FHIR server that persists using local storage. 

At this time, it is set to use the H2 database, which is the easiest to set up but if performance turns out to be undesirable, it may get updated to use Postgres. 

# TODO
## Change DB with the FHIR Version
If you decide to switch versions (R4 to R5 or R4B) it will probably cause errors. We may want to tie the version to the command line so that we can give the db a different name for each version. The current config is set to **R4B**.