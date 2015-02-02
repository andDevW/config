#!/bin/zsh

key=$1
value=$2

echo $value | cat > $key
