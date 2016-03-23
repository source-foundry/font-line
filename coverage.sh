#!/bin/sh

coverage run --source {{PROJECT}} -m py.test
coverage report -m
coverage html

#coverage xml
#codecov --token=$CODECOV_{{fontline}}
