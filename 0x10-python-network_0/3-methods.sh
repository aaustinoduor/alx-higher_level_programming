#!/bin/bash
# Methods
curl -sI "$1" | grep -i '^Allow:' | sed 's/^Allow: //'
