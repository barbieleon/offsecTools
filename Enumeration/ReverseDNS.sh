#!/bin/bash

#Color Variables
PURPLE="\e[35m"
ENDCOLOR="\e[0m"

if [ "$1" == "" ]
then
        printf '\033[31;5m
                            ____             __    _    
                           / __ )____ ______/ /_  (_)__ 
                          / __  / __ `/ ___/ __ \/ / _ \
                         / /_/ / /_/ / /  / /_/ / /  __/
                        /_____/\__,_/_/  /_.___/_/\___/ 
                                                        
                   .__ .___.  ..___.__  __..___  .__ .  . __.
                   [__)[__ \  /[__ [__)(__ [__   |  \|\ |(__ 
                   |  \[___ \/ [___|  \.__)[___  |__/| \|.__)
                                                             
                                                                                                              

        \033[0m\n'


        echo -e "${PURPLE}How to use: ./BarbieReverDNS.sh + target${ENDCOLOR}"
        echo -e "${PURPLE}E.G. ./BarbieReverseDNS.sh 37.59.174${ENDCOLOR}"
else

        printf '\033[31;5m
                            ____             __    _    
                           / __ )____ ______/ /_  (_)__ 
                          / __  / __ `/ ___/ __ \/ / _ \
                         / /_/ / /_/ / /  / /_/ / /  __/
                        /_____/\__,_/_/  /_.___/_/\___/ 
                                                        
                   .__ .___.  ..___.__  __..___  .__ .  . __.
                   [__)[__ \  /[__ [__)(__ [__   |  \|\ |(__ 
                   |  \[___ \/ [___|  \.__)[___  |__/| \|.__)
                                                             
                                                                                                              

        \033[0m\n'




        echo -e "======Subdomains Found======"
        for ip in $(seq 224 239);do host -t ptr $1.$ip;done | grep -v "$1" | cut -d " " -f5
fi