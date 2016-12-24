#!/usr/bin/python

create_db = '''
CREATE TABLE IF NOT EXISTS owners (
    owner_name PRIMARY KEY
);

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

CREATE TABLE IF NOT EXISTS cards (
    card_id INTEGER PRIMARY KEY,
    card_name TEXT NOT NULL,
    type TEXT,
    owner TEXT REFERENCES owners(owner_name) ON UPDATE CASCADE ON DELETE CASCADE,
    used_in_deck INTEGER REFERENCES decks(deck_id) ON UPDATE CASCADE ON DELETE SET NULL
);
'''


import sqlite3
conn = sqlite3.connect('netrunner.db')
c = conn.executescript(create_db)
conn.commit()
conn.close()
