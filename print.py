import sys
import time
from time import sleep

def print_lyrics():
    lines = [
        ("\nWish you'd just talk to me", 0.08),
        
    ]
  
    delays = [0.2]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush() # new line basically
            sleep(char_delay)
        time.sleep(delays[i]) 
        print('')

print_lyrics()
