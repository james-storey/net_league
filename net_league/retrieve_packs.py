#!/usr/bin/env python
# Retrieve the latest pack info direct from netrunnerdb

import sys
import json
import http.client

def run():
    netrunnerdb = http.client.HTTPSConnection('netrunnerdb.com')
    netrunnerdb.request('GET', '/api/2.0/public/cards') # gets all the cards
    card_list = json.load(netrunnerdb.getresponse())
    netrunnerdb.close()

    pack_lists = dict()
    for card in card_list['data']:
        if card['pack_code'] not in pack_lists:
            pack_lists[card['pack_code']] = []
        pack_lists[card['pack_code']].append(card)

    for key in pack_lists:
        pack = open("../packs/" + key + ".json", 'w', encoding='utf-8')
        json.dump(pack_lists[key], pack, indent=2)
        pack.close()

if __name__ == "__main__":
    run()
