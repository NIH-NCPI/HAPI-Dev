# HAPI-Dev
This repository provides some simple helper scripts to launch a local FHIR server that persists using local storage. 

At this time, it is set to use the H2 database, which is the easiest to set up but if performance turns out to be undesirable, it may get updated to use Postgres. 

# TODO
## Figure out how to get R5 working
I honestly think there are changes going on since the last day or two because I have had this working recently but I get strange errors either about lucene or subscription errors on R5 
    * lucene errors occur if I keep the db path the same as the default but use map a local directory to that position. That works just fine for R4B...for now
    * Subscription errors appear to be specific to setting R5 as the version. I have no idea what this is and will check back at some point to see if it is resolved by updates to the image.

# Concerns
I'm a little worried that breaking changes seem to be getting checked into the main hapi-fhir repo. Of course, I may be compiling the docker image wrong, but if that's the case, they should fix the shell script that provides the command I'm using. I just can't get it to compile and I'm not familiar enough with the code nor the build system to know how to go about fixing them myself. 