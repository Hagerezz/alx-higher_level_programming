#!/bin/bash
#takes in a URL
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
