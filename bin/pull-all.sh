#!/bin/bash
for path in ~/Private/code/*; do
    [ -d "${path}" ] || continue;
    directory="$(basename "${path}")";
    cd ${directory};

    #if it's not a git repo, skip it
    if ! [ -d .git ]; then
        cd ~/Private/code;
        continue;
    fi

    echo "Now pulling $directory...";

    #if there were changes, stash them
    CHANGED=$(git diff-index --name-only HEAD --)
    if [ -n "$CHANGED" ]; then
        echo "Stashing...";
        git stash;
    fi

    #check if we're on master
    BRANCH=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p');
    if [ "$BRANCH" != "master" ]; then
        echo "switching from $BRANCH to master"
        git checkout master;
    fi

    git pull --rebase;

    #if we weren't on master, go back to the original branch
    if [ "$BRANCH" != "master" ]; then
        echo "switching back to $BRANCH";
        git checkout $BRANCH;
    fi

    #if there were changes, pop them
    if [ -n "$CHANGED" ]; then
        git stash pop;
    fi

    cd ~/Private/code;
    printf "\n";
done