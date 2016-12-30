#!/usr/bin/python3

import sqlite3
import sys
owner = None
deck_name = None

def build_card_list(card_list):
    for line in card_list.split('\n'):
        if len(line) == 0:
            continue
        num, *title = line.split(' ')
        title = ' '.join(title)
        # Use cards by owner
        # if card not available by deck owner,
        #  flag and add to print out for followup

for i in range(len(sys.argv)):
    if __file__ == sys.argv[i]:
        continue
    if sys.argv[i] == '-n':
        deck_name = sys.argv[i+1]
    elif sys.argv[i] == '-o':
        deck_owner = sys.argv[i+1]
