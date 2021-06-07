from datetime import datetime
import sys
format_string = "%Y-%m-%d %H:%M:%S,%f"

with open("./dates.txt", "r") as f, open("./timestamps.txt", "w") as f1:
    for line in f:
        stripped_line = line.strip()
        date_string = stripped_line[0: 23 ] 
        nanoseconds = stripped_line[-3:]
        print("datestring:",date_string)
        print("nanoseconds:",nanoseconds)
        padded_ns = str(nanoseconds.zfill(6))
        print("padded_ns:",padded_ns)
        try:
            dt_obj = datetime.strptime(date_string, format_string)
            millisec = int(dt_obj.timestamp() * 1000) #millisec
            millisec = str(millisec)
            print("milli before append:",millisec)
            millisec += padded_ns
            nanosec = int(millisec)
            print("nanosec final:",nanosec)
            f1.write(str(nanosec)+"\n")
        except:
            print("Error")