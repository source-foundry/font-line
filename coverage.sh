#!/bin/sh

coverage run --source fontline -m py.test
coverage report -m
coverage html

coverage xml
codecov --token=$CODECOV_FONTLINE
