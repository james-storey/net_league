#!/usr/bin/env python

import json
import sqlite3
import sys

def run(argv):
    db = 'netrunner.db'
    input_filename = None
    owner = None

    for i in range(len(argv)):
        if __file__ == argv[i]:
            continue
        elif '-o' == argv[i]:
            owner = argv[i+1]
        if i == len(argv) - 1:
            input_filename = argv[i]

    input_file = open(input_filename, 'r', encoding='utf-8')
    card_list = json.load(input_file)
    input_file.close()

    conn = sqlite3.connect('netrunner.db')
    for card in card_list:
        for i in range(card['quantity']):
            conn.execute("INSERT INTO"
                + " cards(card_name, type, owner, used_in_deck)"
                + " VALUES(?,?,?,NULL)", [card['title'], card['type_code'], owner])
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run(sys.argv)
