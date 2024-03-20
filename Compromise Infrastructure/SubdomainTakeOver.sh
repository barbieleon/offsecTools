#!/bin/bash

#Color Variables
PURPLE="\e[35m"
ENDCOLOR="\e[0m"

if [ "$1" == "" ] || [[ "$1" && "$2" == "" ]]
then
                printf '\033[31;5m
                            ____             __    _
                           / __ )____ ______/ /_  (_)__
                          / __  / __ `/ ___/ __ \/ / _ \
                         / /_/ / /_/ / /  / /_/ / /  __/
                        /_____/\__,_/_/  /_.___/_/\___/

                 __..  ..__   .___..__..  ..___.__..  ..___.__ 
                (__ |  |[__)    |  [__]|_/ [__ |  |\  /[__ [__)
                .__)|__|[__)    |  |  ||  \[___|__| \/ [___|  \
                                                               
                                                                 


        \033[0m\n'


        echo -e "${PURPLE}How to use: ./BarbieSubTakeOver.sh + target${ENDCOLOR}"
        echo -e "${PURPLE}E.G. ./BarbieSubTakeOver evil.com${ENDCOLOR}"
else
        for subdomains in $(cat $2); do host -t cname $subdomains.$1;done | egrep -v "NXDOMAIN|CNAME"
fi