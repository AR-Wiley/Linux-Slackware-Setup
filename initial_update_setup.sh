#!/bin/bash

set -euo pipefail


if [[ "$EUID" -ne 0 ]]; then
        echo "You must be root to run this script...."
        exit 1
fi

function initial_setup {

        version=$(grep -oP '[0-9]+\.[0-9]+' /etc/slackware-version)

        mirrors_file="/etc/slackpkg/mirrors"

        if [[ ! -e "$mirrors_file" ]]; then
                echo "File does not exist"
                exit 1
        fi

        sed -i "/^#.*slackware\\(64\\)\\?-$version/s/^#//" "$mirrors_file"

}

function update {

        updates=("slackpkg update" "slackpkg install-new" "slackpkg upgrade-all" "slackpkg clean-system")

        for i in "${updates[@]}"; do
                if ! eval "$i"; then
                        echo "'$i' has failed..."
                else
                        echo "'$i' was succuessful..."
                fi
        done

}

initial_setup
update
