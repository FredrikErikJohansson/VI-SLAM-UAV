#!/bin/bash
if [ -z "$1" ] || [ -z "$2" ]
then
    echo "Run with: ./procLDSO.sh <dataset-location> <video-name>"
    exit 1
fi
pwd=`pwd`
cd $1
mkdir images
cd images
mplayer -vo jpeg ../$2.MP4
ls | sed -n 's/\.jpg$//p' >> ../names.txt
cd ..
echo -e "1\n$(cat $2.SRT)" > $2.SRT
awk '0 == NR % 6' $2.SRT >> shutter.txt
echo -e "1\n$(cat $2.SRT)" > $2.SRT
awk '0 == NR % 6' $2.SRT >> dates.txt
sed -i '1,2d' $2.SRT
python3 $pwd/convert.py $1
awk '{print substr($6,3,4)}' shutter.txt >> shutter2.txt
awk '{print sprintf("%.10f", 1000/$1), $2}' shutter2.txt >> shutter3.txt
paste -d" " names.txt timestamps.txt > combined.txt
paste -d" " combined.txt shutter3.txt >> times.txt
rm dates.txt names.txt shutter.txt shutter2.txt shutter3.txt timestamps.txt combined.txt