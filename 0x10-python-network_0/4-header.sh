#!/bin/bash
# Usage: ./get_with_header.sh <URL>
curl -s -H "X-School-User-Id: 98" "$1"
