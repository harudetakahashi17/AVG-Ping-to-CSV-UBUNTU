'''
This program only tested for ubuntu like format like this:

PING 10.0.0.1 (10.0.0.1) 56(84) bytes of data.
64 bytes from 10.0.0.1: icmp_seq=1 ttl=64 time=0.347 ms
64 bytes from 10.0.0.1: icmp_seq=2 ttl=64 time=0.046 ms
64 bytes from 10.0.0.1: icmp_seq=3 ttl=64 time=0.056 ms
64 bytes from 10.0.0.1: icmp_seq=4 ttl=64 time=0.045 ms
64 bytes from 10.0.0.1: icmp_seq=5 ttl=64 time=0.050 ms
64 bytes from 10.0.0.1: icmp_seq=6 ttl=64 time=0.025 ms
64 bytes from 10.0.0.1: icmp_seq=7 ttl=64 time=0.038 ms
64 bytes from 10.0.0.1: icmp_seq=8 ttl=64 time=0.035 ms
64 bytes from 10.0.0.1: icmp_seq=9 ttl=64 time=0.036 ms
64 bytes from 10.0.0.1: icmp_seq=10 ttl=64 time=0.060 ms

--- 10.0.0.1 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9219ms
rtt min/avg/max/mdev = 0.025/0.073/0.347/0.092 ms
'''
import os, os.path

def parseAVG(files):
    # Loop as much as files in DIR
    for count in range(files):
        # Opening the file one by one using variable.
        # Make sure you have uniform name like h2.txt, h3.txt, h4.txt or host1.txt, host2.txt, host3.txt, etc.
        filename = 'puthere/h%s.txt' % (count+2)
        # Open the file in read (r) mode
        f = open(filename, 'r')
        # Checking if the file is in read (r) mode
        if f.mode == 'r':
            # Spliting file by lines
            line = f.read().splitlines()
            # Took the last line of file only
            last = line[-1]
            # Splitting string from 22 character to last character from string last (variable) into new string
            from_min = last[23:]
            # Variable to return only the AVG of RTT
            avg = ''
            # Counter for marking character '/' in min/avg/max/mdev values
            counter = 0
            # Loop to read until end of string
            for i in range(len(from_min)):
                # Assign c as character reader
                c = from_min[i]
                # Just my logic how to get into avg value only
                if c == '/' and counter != 1:
                    counter += 1
                elif c != '/' and counter == 1:
                    # Append string avg with char c
                    avg += c
                elif c == '/' and counter == 1:
                    # After getting the avg value, break it. Not a good way to end loop but whatever
                    break

            # Create a file (if not exist) or open a file in append (a+) mode
            r = open('avg.csv','a+')
            # Write the avg into the file
            r.write(avg + '\n')
            # Close the avg.csv file
            r.close()
        # Close the ping result file
        f.close()

def main():
    # Directory of your ping result in .txt files
    DIR = 'puthere'

    # Counting files in directory
    files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

    # Producing CSV file from all files in DIR
    parseAVG(files)

if __name__ == '__main__':
    main()