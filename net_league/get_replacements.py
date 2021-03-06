#!/usr/bin/env python3
# Use after building a deck that finished incomplete
# This script finds the cards from other owners in the leauge that
#   have the cards needed but are not currently using them
import sqlite3
import sys

def get_deck(conn, deck_owner, deck_name):
    return conn.execute('''SELECT deck_id, card_list FROM decks
        WHERE owner = ? AND deck_name = ? ORDER BY version DESC;
    ''', [deck_owner, deck_name]).fetchone()

def get_candidates(conn, target_deck, even_used):
    missing = []
    deck_id, card_list = target_deck
    for line in card_list.split('\n'):
        if len(line) == 0:
            continue
        num, *title = line.split(' ')
        num = int(num)
        title = ' '.join(title)
        cards = conn.execute('''SELECT card_id FROM cards
            WHERE card_name = ? AND used_in_deck = ?;
        ''', [title, deck_id]).fetchall()
        if len(cards) < num:
            missing.append((num - len(cards), title))
    candidates = {}
    for cardlist in missing:
        card_name = cardlist[1]
        sql = '''SELECT card_id, card_name, owner
            FROM cards WHERE card_name = ? '''
        if even_used == False:
            sql += 'AND used_in_deck IS NULL'
        sql += ';'
        available = conn.execute(sql, [card_name]).fetchall()
        candidates[card_name] = []
        for available_card in available:
            c = {'card_id': available_card[0], 'owner': available_card[2]}
            candidates[card_name].append(c)
    return candidates

def get_replacements(deck_name, deck_owner, card_name, db):
    conn = sqlite3.connect(db)
    target_deck = get_deck(conn, deck_owner, deck_name)
    candidates = get_candidates(conn, target_deck, False)
    conn.close()
    return candidates

def run(argv):
    deck_name = None
    deck_owner = None
    card_name = None
    db = 'card.db'
    for i in range(len(argv)):
        if __file__ == argv[i]:
            continue
        if argv[i] == '-d':
            deck_name = argv[i+1]
        elif argv[i] == '-o':
            deck_owner = argv[i+1]
        elif argv[i] == '-n':
            db = argv[i+1]
    replacements = get_replacements(deck_name, deck_owner, card_name, db)
    print(replacements)

if __name__ == "__main__":
    run(sys.argv)
