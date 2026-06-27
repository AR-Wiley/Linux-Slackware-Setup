#bin/bash

set -euo pipefail

if [[ "$EUID" -ne 0 ]]; then
        echo "You must be root to run this script..."
        exit 1
fi


function System_Update {

        local updates=("apt-get update"
                "apt-get upgrade -y"
                "apt-get dist-upgrade -y"
                "apt-get clean"
                "apt-get autoremove -y")

        for i in "${updates[@]}"; do
                if ! bash -c "$i"; then
                        echo "'$i' Failed"
                        exit 1
                fi
        done

        echo "Update Completed"
}


function set_hostname {

        local hostname=$1

        hostname_file="/etc/hostname"

        if [[ ! -e "hostname_file" ]];
                echo "Hostname File does not exist.."
                exit 1
        fi

        truncate -s 0 "hostname_file"

        echo $1 >> "hostname_file"
}


function set_ip_address {

        local ipaddress=$1
        local gateway=$2
        local ifname="{$3:-eth0}"
        local dhcp="{$4:-"no"}"

        inet_file="/etc/rc.d/rc.inet1.conf"

        if [[ ! -e "inet_file" ]];
                echo "Inet File does not exist.."
                exit 1
        fi
}
