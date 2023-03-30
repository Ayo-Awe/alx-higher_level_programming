#!/usr/bin/env bash
# Script to display body of 200 responses
curl --head -s "$1" | head -n 1 | grep "200" > /dev/null && curl -s "$1"
