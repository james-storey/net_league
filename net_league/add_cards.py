#!/usr/bin/env python

import json
import sqlite3
import sys

def run(argv):
    db = 'netrunner.db'
    input_file = None
    owner = None

    for i in range(len(argv)):
        if __file__ == argv[i]:
            continue
        elif '-o' == argv[i]:
            owner = argv[i+1]
        if i == len(argv) - 1:
            input_file = argv[i]

    pack_name = ''
    filename = ''
    if input_file.find('.json') > -1:
        filename = input_file
        pack_name = input_filename.split('.')[0]
    else:
        filename = input_file + '.json'
        pack_name = input_file
    f = open(filename, 'r', encoding='utf-8')
    card_list = json.load(f)
    f.close()

    conn = sqlite3.connect('netrunner.db')
    for card in card_list:
        for i in range(card['quantity']):
            conn.execute('''
                INSERT INTO cards(
                    card_name, type, pack, owner, used_in_deck
                )
                VALUES(?,?,?,?,NULL)
            ''', [card['title'], card['type_code'], pack_name, owner])
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run(sys.argv)
