#!/bin/zsh
startd=$(pwd)

green='\e[32m'
red='\e[31m'
endColor='\e[0m'

buildSbts=$(find . -name "build.sbt" -exec dirname {} \; | grep -v "\.ensime_cache")
buildScalas=$(find . -name "Build.scala" -exec dirname {} \; | grep -v "\.ensime_cache" | sed s/project//)

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

    cd $startd
done

echo "$green\nALL DONE$endColor"
