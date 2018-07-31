#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size
curl -sI "$1" |grep -i Content-length | awk "{print "$2"}"
