#!/usr/bin/env bash
# Script to print http status code
curl -o /tmp/file  -sw "%{http_code}" "$1"
