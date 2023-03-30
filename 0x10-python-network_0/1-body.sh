#!/bin/bash
# Script to display body of 200 responses
curl -si "$1" | head -n 1 | grep "200" > /dev/null && curl -s "$1"
