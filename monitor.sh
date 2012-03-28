#!/bin/bash

sha=0
previous_sha=0

update_sha()
{
    sha=`ls -lR *.py test/*.py | shasum`
}

build () {
    ## Build/make commands here
    echo
    echo "--> Monitor: Monitoring filesystem... (Press enter to force a build/update)"
    ./test.sh
}

changed () {
    echo "--> Monitor: Files changed, Building..."
    build
    previous_sha=$sha
}

compare () {
    update_sha
    if [[ $sha != $previous_sha ]] ; then changed; fi
}

run () {
    while true; do

        compare

        read -s -t 1 && (
        echo "--> Monitor: Forced Update..."
        build
        )

    done
}

echo "--> Monitor: Init..."
echo "--> Monitor: Monitoring filesystem... (Press enter to force a build/update)"
run
