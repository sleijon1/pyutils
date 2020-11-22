import argparse
import sys
import os
import requests

"""
Module for automatically creating Advent of Code
directory with input gathered via cookie authentication.

Author: Simon Leijon
Github: sleijon1
"""

parser = argparse.ArgumentParser(
    description='Creates folder and gathers\
    personal Advent of Code input. \
    To get personal input from advent of code: \
    add personal cookie to file "cookie.txt" in the directory \
    you run the script from. \
    example usage: initfolder.py 2020 14',
    usage='%(prog)s year day...',
    epilog='Good look puzzling!')

parser.add_argument('year',
                    help='The year of the calender. ex: 2018',
                    action="store")
parser.add_argument('day',
                    help='The day of the calender. ex: 19',
                    action="store")
parser.add_argument('-ft',
                    help='if specified creates file with the \
                    specified file type to write your solution in. \
                    example usage: -ft py',
                    action="store")

path = os.getcwd()
args = parser.parse_args()

try:
    cookie = open("cookie.txt").read().strip()
except FileNotFoundError:
    print("Error: Specify your cookie in a file with name cookie.txt")
    sys.exit()

headers = {'session': cookie}
session = requests.Session()
year, day = args.year, args.day

dirname = 'day' + str(day)
try:
    os.mkdir(path+'/'+dirname)
except FileExistsError:
    print("Directory with name \"%s\" already exists." % dirname)
    sys.exit()
print("Created dir: \"%s\"" % dirname)

if args.ft is not None:
    file_name = dirname+'.'+args.ft
    with open(path+'/'+dirname+'/'+file_name, 'w') as input_file:
        input_file.close()
        print("Created file: \"%s\" " % file_name)

url = f'https://adventofcode.com/{year}/day/{day}/input'
resp = session.get(url, cookies=headers)
resp.raise_for_status()
with open(path+'/'+dirname+'/'+'input.txt', 'w') as input_file:
    input_file.write(resp.text)
print(f"Successfully gathered input for Advent of Code year {year}, day {day}.")
