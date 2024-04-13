#!/bin/bash

function install() {
    clear

    echo -e "\033[31m[~] Instalando phoneinfoga..."

    arch=$(uname -m)

    if [[ $arch == *"arm"* || $arch == *"Android"* ]]; then
        url='https://github.com/sundowndev/phoneinfoga/releases/download/v2.10.8/phoneinfoga_Linux_armv6.tar.gz'
    elif [[ $arch == *"x86_64"* ]]; then
        url='https://github.com/sundowndev/phoneinfoga/releases/download/v2.10.8/phoneinfoga_Linux_x86_64.tar.gz'
    else
        url='https://github.com/sundowndev/phoneinfoga/releases/download/v2.10.8/phoneinfoga_Linux_i386.tar.gz'
    fi

    url_n=$(basename "$url")
    wget "$url" && tar -xvzf "$url_n"
    mv phoneinfoga phoneinf/
    rm "$url_n"

    echo -e "\033[34m\n[~] Instalando dependencias...\n"
    pip3 install -r requirements.txt

    echo -e "\n\033[32m[ ✔ ] Instalación completa."
}

install