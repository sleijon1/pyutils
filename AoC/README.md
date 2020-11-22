# AoC Input via requests
Automatically gathers personal AoC input.
Specify your personal cookie in the directory you're running the script from.

To get your cookie:
1. Go to [AoC](https://adventofcode.com/)
2. Login and open the network monitor
3. Press Headers -> copy the session cookie
4. Paste it into **cookie.txt** in the directory you are running the script from

Then run the script in the directory where you want to keep your solution and input.

Running: *aoc-input.py 2017 18 -ft py* 

Creates:
```
day18
|-- day18.py
|-- input.txt (Contains personal input)
```


