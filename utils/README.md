# Utils

### Extract frames from video:
Extract frames from video using MPlayer:
* `mplayer -vo jpeg myVideo.mp4` and zip them: `zip -r myZip .`

### Lower the number of samples:
Copy files without any special characters if `????? % <num> = 1`, using: 
* `cp $(printf '%s\n' consistent_name_?????.jpg | awk 'NR%<num> == 1') <location>`

### Extract data from csv:
Extract colums from csv to new csv:
* `awk -F"," '{print $1,$2}' in.csv > out.csv` gives `col1 col2`
* `awk -F"," '{print $1","$2}' in.csv > out.csv` gives `col1,col2`
* `awk -F"," '{print $1","$2",0.1"}' in.csv > out.csv` gives `col1,col2,0.1`

### Combine two csv files
* `paste -d"," one.csv two.csv > combined.csv`

### Compile cameracalib.cpp
* ``g++ cameracalib.cpp -o cameracalib `pkg-config --cflags --libs opencv` ``

### Extract certain rows from file
* `awk '0 == NR % <num>' input.SRT >> times.txt`

### Data pre-processing for DJI Mavic 2
LDSO:
* `./procLDSO.sh /absolute/path/to/dataset example-video`

ORB_SLAM3:
* `./procORB.sh /absolute/path/to/dataset example-video`

### Compute mean error of a pointcloud to its ground-truth
* `./meanError plyExample plyExampleGroundTruth`
