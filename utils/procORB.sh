#!/bin/bash
if [ -z "$1" ] || [ -z "$2" ]
then
    echo "ERROR: Missing arguments"
	echo "Run with: ./procORB.sh /absolute/path/to/dataset example-video"
    exit 1
fi
pwd=`pwd`
cd $1
echo "Extracting frames:"
if [ ! -d "./images" ]
then
	mkdir images
	cd images
	mplayer -vo jpeg ../$2.MP4
	echo "Frames extracted!"
else 
	echo "Frames already extracted!"
	cd images
fi
echo "Constructing text file:"
ls | sed -n 's/\.jpg$//p' >> ../names.txt
cd ..
echo -e "1\n1\n$(cat $2.SRT)" > $2.SRT
awk '0 == NR % 6' $2.SRT >> dates.txt
sed -i '1,2d' $2.SRT
python3 $pwd/convert.py $1
paste -d"," timestamps.txt names.txt >> $2.txt
sed -i '$d' $2.txt
echo "Finished!"
rm dates.txt names.txt timestamps.txt

