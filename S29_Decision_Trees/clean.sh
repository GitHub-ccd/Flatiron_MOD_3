#!/bin/bash -l 

#sed -i 's/$/\.git/' links.txt

while read i
do 
  echo $i 
  dir=`echo $i | sed 's/https:\/\/github.com\/learn-co-students\///'`
  #rm $dir/.gitignore
  rm -r $dir/.git
done < links.txt