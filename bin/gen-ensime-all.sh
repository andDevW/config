#!/bin/zsh
startd=$(pwd)
root="/var/lucid"

green='\e[32m'
red='\e[31m'
endColor='\e[0m'

cd $root

buildSbts=$(find . -name "build.sbt" -exec dirname {} \; | grep -v "\.ensime_cache")
buildScalas=$(find . -name "Build.scala" -exec dirname {} \; | grep -n "\.ensime_cache" | sed s/project//)

paths="$(echo $buildSbts) $(echo $buildScalas)"

echo $paths | tr ' ' '\n' | while read dir; do
    echo $green
    echo "Starting: $dir$endColor"
    echo $endColor

    cd $dir
    sbt gen-ensime
    if [ $? -ne 0 ]; then
        echo "$red\nERROR ON $dir\n$endColor"
    else
        echo "$green\nSuccess on $dir\n$endColor"
    fi

    cd $root
done

cd $startd

echo "$green\nALL DONE$endColor"
