#!/bin/bash

set -euo pipefail


if [[ "$EUID" -ne 0 ]]; then
        echo "You must be root to run this script...."
        exit 1
fi

function initial_setup {

        version=$(grep -oP '[0-9]+\.[0-9]+' /etc/slackware-version)

        mirrors_path="/etc/slackpkg/mirrors"

        if [[ ! -d "$mirrors_path" ]]; then
                echo "Path does not exist"
                exit 1
        fi

        sed -i "/^#.*slackware\\(64\\)\\?-$version/s/^#//" "$mirrors_path"

}

initial_setup
