#!/bin/bash
if [ -z "$1" ] || [ -z "$2" ]
then
    echo "Run with: ./procORB.sh <dataset-location> <video-name>"
    exit 1
fi
pwd=`pwd`
cd $1
mkdir images
cd images
mplayer -vo jpeg ../$2.MP4
ls | sed -n 's/\.jpg$//p' >> ../names.txt
cd ..
echo -e "1\n1\n$(cat $2.SRT)" > $2.SRT
awk '0 == NR % 6' $2.SRT >> dates.txt
sed -i '1,2d' $2.SRT
python3 $pwd/convert.py $1
paste -d"," timestamps.txt names.txt >> $2.txt
rm dates.txt names.txt timestamps.txt

