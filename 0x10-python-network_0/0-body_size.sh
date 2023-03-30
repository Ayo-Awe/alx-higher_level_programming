#!/usr/bin/env bash
# Script to send a request to that URL
curl --head -s "$1" | grep "Content-Length:" | cut -d " " -f 2
