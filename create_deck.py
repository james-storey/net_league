#!/usr/bin/python3

import sqlite3
import sys
deck_filename = None
owner = None
deck_name = None

#def parse_deck(deck_file):
#    for line in deck_file.split('\n'):
#        num, *title = line.split(' ')
#        title = ' '.join(title)
#

def check_card_list_syntax(card_list):
    for line in deck_file.split('\n'):
        num, *title = line.splite(' ')
        title = ' '.join(title)
        try:
            num = int(num)
        except ValueError:
            return False
    return True

for i in len(sys.argv):
    if __file__ == sys.argv[i]:
        continue
    if sys.argv[i] == '-o':
        owner = sys.argv[i+1]
    elif sys.argv[i] == '-n':
        deck_name = sys.argv[i+1]
    elif sys.argv[i] == '-f':
        deck_filename = sys.argv[i+1]
    elif i == len(sys.argv) - 1 and deck_filename is None:
        deck_filename = sys.argv[i]

if owner is None:
    print('No owner specified, Exiting')
    sys.exit(1)
if deck_name is None:
    print('No deck name specified, Exiting')
    sys.exit(1)

f = open(deck_filename, 'r')
card_list = f.read()
f.close()
if check_card_list_syntax(card_list) == False:
    print('card list syntax error: expecting jenteki.net syntax, Exiting')
    sys.exit(1)

conn = sqlite3.connect('netrunner.db')
conn.execute('''
    INSERT INTO decks(deck_name, owner, card_list)
    VALUES(?, ?, ?);
''', [deck_name, owner, card_list])
conn.commit()
conn.close()
