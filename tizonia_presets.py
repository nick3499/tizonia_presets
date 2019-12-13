#!/usr/bin/env python3
# $ python3 tizonia_presets.py
from csv import reader  # encode CSV data
from subprocess import run  # execute args in CLI

urls = {}  # store: numerical keys/URL values

with open('track_links.csv', newline='') as csv_encode:
    csv_read = reader(csv_encode, delimiter=',')  # encoded wrapper
    print(f'{csv_encode.readline()}')  # header (1st line of CSV file)
    c = 1  # initialize counter
    for rec in csv_read:
        print(f'{c:>2}: {rec[0]}')  # number/title
        urls[c] = rec[1]  # insert keys/values into `urls` dict
        c += 1  # increment counter

trk_num = int(input('\x1b[1;36mEnter track number\x1b[0m: '))  # get track num
run(["tizonia", "--youtube-audio-stream", urls[trk_num]])  # start tizonia
