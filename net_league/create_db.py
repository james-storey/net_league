#!/usr/bin/env python

import sqlite3

create_db = '''
CREATE TABLE IF NOT EXISTS owners (
    owner_name PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS decks (
    deck_id INTEGER PRIMARY KEY,
    deck_name TEXT NOT NULL,
    active INTEGER DEFAULT 0,
    owner TEXT,
    card_list TEXT,
    wins INTEGER DEFAULT 0,
    loses INTEGER DEFAULT 0,
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

CREATE TABLE IF NOT EXISTS games (
    game_id INTEGER PRIMARY KEY,
    winning_deck INTEGER REFERENCES decks(deck_id) ON UPDATE CASCADE ON DELETE SET NULL,
    losing_deck INTEGER REFERENCES decks(deck_id) ON UPDATE CASCADE ON DELETE SET NULL,
    game_date TEXT,
    notes TEXT
);
'''

def run():
    conn = sqlite3.connect('netrunner.db')
    conn.executescript(create_db)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    run()
