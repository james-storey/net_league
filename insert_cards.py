#!/usr/bin/python

import json
import sqlite3
import sys

db = 'netrunner.db'
input_filename = None
owner = None

for i in range(len(sys.argv)):
    if __file__ == sys.argv[i]:
        continue
    elif '-o' == sys.argv[i]:
        owner = sys.argv[i+1]
    if i == len(sys.argv) - 1:
        input_filename = sys.argv[i]

input_file = open(input_filename, 'r')
card_list = json.load(input_file)
input_file.close()

conn = sqlite3.connect('netrunner.db')
for card in card_list:
    for i in range(card['qty']):
        conn.execute("INSERT INTO"
            + " cards(card_name, type, owner, used_in_deck)"
            + " VALUES(?,?,?,NULL)", [card['name'], card['type'], owner])
conn.commit()
conn.close()
