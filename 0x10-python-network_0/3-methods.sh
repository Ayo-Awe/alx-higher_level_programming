#!/bin/bash
# Script to display allowed http methods
curl --head -s "$1" | grep "Allow" | cut -d " " -f 2,3,4
