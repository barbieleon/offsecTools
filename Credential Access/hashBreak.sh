#!/usr/bin/bash

if [ "$1" == "" ]
then
	echo "BARBIE HASH BREAKER"
	echo "How to use: ./hashBreaker.sh + wordlist + hash function"
	echo "Eg: ./hashBreaker.sh wordlist sha1sum"
else
	for hashBreaker in $(cat $1);do echo -n $hashBreaker " ";echo -n $hashBreaker | $2;done >> rainbowtables.txt
fi