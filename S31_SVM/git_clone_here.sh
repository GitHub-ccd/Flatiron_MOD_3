#!/bin/bash -l 

#sed -i 's/$/\.git/' links.txt

while read i; do  git clone $i ; done < links.txt