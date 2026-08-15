#!/bin/bash

set -euo pipefail


if [[ "$EUID" -ne 0 ]]; then
        echo "You must be root to run this script...."
        exit 1
fi

 mirrors_file="/etc/slackpkg/mirrors"
 updates=("slackpkg update" "slackpkg install-new" "slackpkg upgrade-all" "slackpkg clean-system")

function initial_setup {

        local version=$(grep -oP '[0-9]+\.[0-9]+' /etc/slackware-version)

        if [[ ! -e "$mirrors_file" ]]; then
                echo "File does not exist"
                exit 1
        fi

        sed -i 's|^[^#]|#&|' "$mirrors_file"
        sed -i "/slackware\\(64\\)\\?-$version/{s/^#//;q;}" "$mirrors_file"

}

function update {

        for i in "${updates[@]}"; do
                if ! eval "$i"; then
                        echo "'$i' has failed..."
                else
                        echo "'$i' was successful..."
                fi
        done

}

initial_setup
update
