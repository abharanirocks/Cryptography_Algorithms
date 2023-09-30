#!/bin/bash

echo "enter filename"
read NAME
var=${NAME}.py
echo "filename: $var"

python $var 
echo Done!
# ./$NAME