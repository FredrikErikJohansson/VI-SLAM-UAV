# Utils

### Extract frames from video:
Extract frames from video using MPlayer:
* `mplayer -vo jpeg <video>` and zip them: `zip -r <name> <location>`.

### Lower the number of samples:
Copy files without any special characters if `???? % <num> = 1`, using: 
* `cp $(printf '%s\n' consistent_name_?????.jpg | awk 'NR%<num> == 1') <location>`

### Extract data from csv:
Extract colums from csv to new csv:
* `awk -F"," '{print $1,$2}' in.csv > out.csv` gives `col1 col2`
* `awk -F"," '{print $1","$2}' in.csv > out.csv` gives `col1,col2`
