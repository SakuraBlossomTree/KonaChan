#!/bin/bash

cd pics

a=0
for i in *.jpg; do
  new=$(printf "%04d.jpg" "$a") #04 pad to length of 4
  if [ ! -f $new ]; then
    mv -i -- "$i" "$new"
    let a=a+1
  fi
done

for i in *.JPG; do
  new=$(printf "%04d.jpg" "$a") #04 pad to length of 4
  if [ ! -f $new ]; then
    mv -i -- "$i" "$new"
    let a=a+1
  fi
done


NUM=$(ls *.jpg | wc -l)

for i in $(seq 0 $NUM)
do
    i=$(printf "%04d" "$i")

    feh --bg-fill $i.jpg
  
    sleep 1 

done

cd ..
