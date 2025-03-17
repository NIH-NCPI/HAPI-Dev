#!/usr/bin/env python

import argparse
from pathlib import Path
from subprocess import run
import os
import sys

import pdb

parser = argparse.ArgumentParser(description="Start FHIR Server")

parser.add_argument("--fhir-version", choices=("R4", "R4B", "R5"), default="R4B")

parser.add_argument(
    "-cd",
    "--config-dir",
    default="cfg",
    help="The path containing the directories for each of the supported versions. This directory must contain a directory named after the fhir-version to be used which contains a file named app.yaml. The default configurations also point to a package file inside this directory which contains the IG to be loaded.",
)

parser.add_argument(
    "--config-filename",
    default="app.yaml",
    help="FHIR Configuration (YAML) to be used.",
)

parser.add_argument(
    "-p", "--port", default=8080, type=int, help="Local port for the server to listen"
)

parser.add_argument(
    "-d",
    "--detach",
    action="store_true",
    help="When present, the container will be detached and run in the background. Please note, the container ID will be shown in stdout.",
)
parser.add_argument(
    "-n",
    "--container-name",
    default="hapi-fhir",
    help="Name to be used for the running container",
)
parser.add_argument(
    "-i",
    "--image-name",
    default="hapiproject/hapi:latest",
    help="Docker Image to be loaded",
)

parser.add_argument("--db", default="db", help="Database Directory on Local System")
args = parser.parse_args()

if not Path(args.config_dir).exists():
    sys.stderr.write(
        f"The specified configuration directory, {args.config_dir} doesn't exist. This directory should contain a directory named after the desired FHIR Version (R4, R4B, etc) which contains the YAML file containing the FHIR configuraiton named 'app.yaml'."
    )

config_dir = Path(args.config_dir).resolve() / args.fhir_version

config_fn = config_dir / args.config_filename

dbdir = Path(args.db)
dbdir.mkdir(parents=True, exist_ok=True)

cmd = [
    "docker",
    "run",
    "--rm",
    "-p",
    f"{args.port}:8080",
    "-v",
    f"{dbdir.resolve()}:/app/database",
    "-v",
    f"{config_dir}:/configs",
    "-e",
    f'"--spring.config.location=file:///configs/{args.config_filename}"',
]
if args.detach:
    cmd.append("-d")

cmd += [
    args.image_name,
    "-n",
    args.container_name,
]

print(" ".join(cmd))
os.system(" ".join(cmd))  # , capture_output=True)
