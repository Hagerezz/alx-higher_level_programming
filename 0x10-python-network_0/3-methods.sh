#!/bin/bash
#takes in a URL and displays all HTTP 
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
