#!/bin/bash

#Color Variables
CYAN="\e[36m"
ENDCOLOR="\e[0m"

printf '\033[35;5m
                            ____             __    _    
                           / __ )____ ______/ /_  (_)__ 
                          / __  / __ `/ ___/ __ \/ / _ \
                         / /_/ / /_/ / /  / /_/ / /  __/
                        /_____/\__,_/_/  /_.___/_/\___/ 
                                                        
                        +-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+
                        |B|r|u|t|e| |F|o|r|c|e| |D|N|S|
                        +-+-+-+-+-+ +-+-+-+-+-+ +-+-+-+

        \033[0m\n'

echo -e "\n"
echo -e "\n"
echo -e "\n"

if [[ "$1" == "" ]] || [[ "$1" && "$2" == "" ]]
then
        echo -e "${CYAN}How to use: ./BarbieBruteForceDns.sh + target + wordlist${CYAN}${ENDCOLOR}"
        echo -e "${CYAN}E.G.  ./BarbieBruteForceDNS.sh evil.com barbieWordlist.txt${CYAN}${ENDCOLOR}"
else


        echo -e "${CYAN}======SUBDOMAINS FOUND======${CYAN}${ENDCOLOR}"
        for subdomains in $(cat $2);do host $subdomains.$1;done | grep -v "NXDOMAIN"
fi