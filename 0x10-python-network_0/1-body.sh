#!/usr/bin/env bash
# Script to display body of 200 responses

status=$(curl --head -s "$1" | head -n 1 | cut -d ' ' -f 2)
if [[ status -eq 200 ]]
then
	curl -s "$1"
fi
