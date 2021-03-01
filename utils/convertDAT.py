from datetime import datetime, timedelta
import sys
format_string = "%Y-%m-%dT%H:%M:%SZ"
with open("./dates.txt", "r") as f, open("./milliseconds.txt", "r") as f1, open("./DATtimes.txt", "w") as f2:
    for line in f:
        stripped_line = line.strip()
        try:
            dt_obj = datetime.strptime(stripped_line, format_string)
            millisec = int(dt_obj.timestamp() * 1000)
            millisec = millisec + 3600000 # add one hour to conform to SRT timestamps
            VIOmilli = int(f1.readline())
            if (VIOmilli < 0): # catch bad values
                VIOmilli = 0
            else:
                millisec = millisec + VIOmilli
            f2.write(str(millisec)+"\n")
        except: 
            print("Error")