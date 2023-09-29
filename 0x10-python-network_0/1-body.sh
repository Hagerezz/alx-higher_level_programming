#!/bin/bash
#command
curl -sI "$1" | grep -q "HTTP/1.1 200 OK" && curl -s "$1"
