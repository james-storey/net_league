#!/usr/bin/python

create_owners = '''
CREATE TABLE IF NOT EXISTS owners (
    owner_name PRIMARY KEY
);
'''
create_decks = '''
CREATE TABLE IF NOT EXISTS decks (
    deck_id INTEGER PRIMARY KEY,
    deck_name TEXT NOT NULL,
    identity TEXT,
    active INTEGER DEFAULT 0,
    owner TEXT,
    scheme TEXT,
    wins INTEGER,
    loses INTEGER,
    created TEXT DEFAULT CURRENT_DATE,
    FOREIGN KEY(owner)
        REFERENCES owners(owner_name)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
'''
create_cards = '''
CREATE TABLE IF NOT EXISTS cards (
    card_id INTEGER PRIMARY KEY,
    card_name TEXT NOT NULL,
    owner TEXT REFERENCES owners(owner_name) ON UPDATE CASCADE ON DELETE CASCADE,
    used_in_deck INTEGER REFERENCES decks(deck_id) ON UPDATE CASCADE ON DELETE SET NULL
);
'''


import sqlite3
conn = sqlite3.connect('netrunner.db')
c = conn.cursor()
c.execute(create_owners)
c.execute(create_decks)
c.execute(create_cards)
conn.commit()
conn.close()
