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
	echo "Zipping frames:"
	zip -r ../images .
	echo "Frames zipped!"
else 
	echo "Frames already extracted!"
	cd images
fi
echo "Constructing text file:"
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
sed -i '$d' times.txt
cp $pwd/camera.txt ./camera.txt
echo "Finished!"
rm dates.txt names.txt shutter.txt shutter2.txt shutter3.txt timestamps.txt combined.txt
