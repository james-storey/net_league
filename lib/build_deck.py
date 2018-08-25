#!/bin/usr/env python3
# build a deck for the given user with the starting state in the repository

import toml

def lookup_card(title):
	# lookup info from master list

def add_card(info, quantity):
	# sanity check before returning op

def parse_jenteki_deck(deckstring):
	ops = []
	decklist = deckstring.splitlines()
	for line in decklist:
		(quantity, sep, name) = line.partition(" ")
		ops.append(add_card(lookup_card(name), quantity))
	return ops

def build_deck(owner, name):
	user_packs_file = "../users/{0}/cards/packs.toml".format(owner)
	user_deck_file = "../users/{0}/decks/{1}.toml".format(owner, name)
	deck = toml.loads(user_deck_file)
	ops = parse_jenteki_deck(deck["deck"])

	user_packs = toml.load(user_packs_file)
	for op in ops:
		# check that user has cards in the appropriate quantity
		# if not, check other owners for copies
		# if still not, throw error
		card_owner = owner
		user_packs[op.pack_id][op.title] = { 
			"in": name, 
			"q": op["quantity"], 
			"owner": card_owner 
		}
	toml.dump(user_packs, user_packs_file)

def run(argv):
	arguments = argv[1:]
	deck_name = None
	deck_owner = None
	for i in range(len(arguments), 2):
		label = arguments[i]
		value = arguments[i+1]
		if label == "-n" or label == "--name":
			deck_name = value
		elif label == "-o" or lable == "--owner":
			deck_owner = value
	result = build_deck(deck_owner, deck_name)
	print(result)

if __name__ == "__main__":
	run(sys.argv)