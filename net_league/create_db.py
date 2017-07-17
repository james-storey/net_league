#!/usr/bin/env python3

import sqlite3

create_db = '''
CREATE TABLE IF NOT EXISTS owners (
    owner_name PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS decks (
    deck_id INTEGER PRIMARY KEY,
    deck_name TEXT NOT NULL,
    version INTEGER DEFAULT 1,
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

CREATE TABLE IF NOT EXISTS games (
    game_id INTEGER PRIMARY KEY,
    winning_deck INTEGER REFERENCES decks(deck_id) ON UPDATE CASCADE ON DELETE SET NULL,
    losing_deck INTEGER REFERENCES decks(deck_id) ON UPDATE CASCADE ON DELETE SET NULL,
    game_date TEXT,
    notes TEXT
);
'''

nr_cards = '''

CREATE TABLE IF NOT EXISTS cards (
    card_id INTEGER PRIMARY KEY,
    card_name TEXT NOT NULL,
    type TEXT,
    pack TEXT,
    owner TEXT REFERENCES owners(owner_name) ON UPDATE CASCADE ON DELETE CASCADE,
    used_in_deck INTEGER REFERENCES decks(deck_id) ON UPDATE CASCADE ON DELETE SET NULL
);
'''

mtg_cards = '''

CREATE TABLE IF NOT EXISTS cards (
    card_id INTEGER PRIMARY KEY,
    card_name TEXT NOT NULL,
    color TEXT,
    type TEXT,
    cmc TEXT,
    'set' TEXT,
    owner TEXT REFERENCES owners(owner_name) ON UPDATE CASCADE ON DELETE CASCADE,
    used_in_deck INTEGER REFERENCES decks(deck_id) ON UPDATE CASCADE ON DELETE SET NULL
);
'''

def create_db(db_name, db_type):
    create_script = None
    if db_type == 'nr':
        create_script = create_db + nr_cards
    elif db_type == 'mtg':
        create_script = create_db + mtg_cards
    conn = sqlite3.connect(db_name)
    conn.executescript(create_db)
    conn.commit()
    conn.close()

def run(argv):
    db_name = 'card.db'
    db_type = 'nr'
    for i in range(len(argv)):
        if __file__ == argv[i]:
            continue
        if argv[i] == '-n':
            db_name = argv[i+1]
        elif argv[i] == '-t':
            db_type = argv[i+1]
    create_db(db_name, db_type)
    
if __name__ == "__main__":
    run(sys.argv)
