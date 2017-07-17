#!/usr/bin/env python
# Use this script to add cards by data pack to the users tableau of cards.
# This script will not check if you add from the same data pack twice
# check that you do not already have the pack with the inspect_db script
import json
import sqlite3
import sys
import os

insert_mtg = '''
INSERT INTO cards(
    card_name, color, type, cmc, run, owner, used_in_deck
)
VALUES(?,?,?,?,?,?,NULL)
'''

insert_nr = '''
INSERT INTO cards(
    card_name, type, pack, owner, used_in_deck
)
VALUES(?,?,?,?,NULL)
'''

def add_cards(card_list, owner, db):
    conn = sqlite3.connect(db)
    for card in card_list:
        for i in range(card['quantity']):
            if type == 'mtg':
                query = insert_mtg
                conn.execute(query,
                    card_list['title'],
                    card_list['color'],
                    card_list['type_code'],
                    card_list['cmc'],
                    card_list['set'],
                    owner
                )
            elif type == 'nr':
                query = insert_nr
                conn.execute(query,
                    card_list['title'],
                    card_list['type_code'],
                    pack_name,
                    owner
                )
    conn.commit()
    conn.close()

def run(argv):
    db = 'card.db'
    input_file = None
    owner = None
    type = 'nr'

    for i in range(len(argv)):
        if __file__ == argv[i]:
            continue
        elif '-o' == argv[i]:
            owner = argv[i+1]
        elif '-n' == argv[i]:
            db = argv[i+1]
        elif '-t' == argv[i]:
            type = argv[i+1]
        if i == len(argv) - 1:
            input_file = argv[i]


    # deserialize the card manifest
    pack_name = ''
    filename = ''
    if input_file.find('.json') > -1:
        filename = input_file
        if type == 'nr':
            pack_name = os.path.basename(input_file).split('.')[0]
    else:
        filename = input_file + '.json'
        if type == 'nr':
            pack_name = os.path.basename(input_file)
    f = open(filename, 'r', encoding='utf-8')
    card_list = json.load(f)
    f.close()
    add_cards(card_list, owner, db)
    
if __name__ == "__main__":
    run(sys.argv)
