#!/usr/bin/env bash
dir=$(pwd -P)
docker run -it --name mod_p --rm -v $dir:/var/opt python:3.7.0-alpine3.8 /bin/sh
