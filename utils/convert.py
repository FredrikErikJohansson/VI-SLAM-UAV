from datetime import datetime
import sys
format_string = "%Y-%m-%d %H:%M:%S,%f"

print (sys.argv[1])

with open(sys.argv[1] + "/dates.txt", "r") as f, open(sys.argv[1] + "/timestamps.txt", "w") as f1:
    for line in f:
        stripped_line = line.strip()
        truncated_line = stripped_line[:-4] # remove nanoseconds
        try:
            dt_obj = datetime.strptime(truncated_line, format_string)
            millisec = int(dt_obj.timestamp() * 1000)
            f1.write(str(millisec)+"\n")
        except: 
            print("Error")
