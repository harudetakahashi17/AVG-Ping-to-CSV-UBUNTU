# AVG-Ping-to-CSV-UBUNTU
Parse the last line of output ping in Ubuntu and take only avg time and save it to csv file.

# Limitation of Use
This program made using python and only tested on ubuntu-like ping output format, example ubuntu ping output:

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

And that output is saved on uniform filename like h1.txt, h2.txt, h3.txt or h1-to-h2.txt, h1-to-h3.txt, etc. You'll know what I mean..

# How to Use
1. Download or copy the code
2. Place the code in specific folder
3. Within the folder in same place with the code, make new folder called 'puthere' for put all your ping result files.
4. Type in terminal $ python avgping.py (MAKE SURE YOU ARE IN CORRECT DIRECTORY)
5. Wait a few seconds, and Done!

# Note
You can modify the code to satisfy your needs. Happy Code ;)
