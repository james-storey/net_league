#!/usr/bin/env python3

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

def run(argv):
    for i in range(len(argv)):
        if __file__ == argv[i]:
            continue
        if argv[i] == '-n':
            deck_name = argv[i+1]
        elif argv[i] == '-o':
            deck_owner = argv[i+1]

if __name__ == "__main__":
    run(argv)
