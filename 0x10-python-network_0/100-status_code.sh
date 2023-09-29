#!/bin/bash
# Usage: ./get_status_code.sh <URL>
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
