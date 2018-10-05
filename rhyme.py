import urllib, urllib2
from lxml import html
import requests
import sys
import string
import re
import random
import math
import pronouncing
import nltk
import operator

def rh(w, c):
	word = w.split()[-1]
	candidate = c.split()[-1]
	rhymes = pronouncing.rhymes(word)	
	rhymes = [x.encode('utf-8') for x in rhymes]

	if candidate in rhymes:
		return True
	elif candidate[-4:] == word[-4:] and w != c:
		return True
	return False 

cards = []
toCheck = []

with open('/home/helen/rhyme/raw.txt','r+') as f:

	#card_count = f.readline()

	for card in f:
		cards.append(card)
		toCheck.append(card)

counts = {}

print('read cards')

i = 0
cards_size = len(cards)
with open("/home/helen/rhyme/rhymes.txt", 'r+') as f:

#	for i in xrange(len(cards) - 1, -1, -1):
	while len(cards) > 0:

		card = cards[0]
		this_count = 0
		f.write(card)


		for j in range(0, len(toCheck)):
			other_card = toCheck[j]
			if rh(card, other_card):
				f.write('   ' + other_card)
				cards[:] = (value for value in cards if value != card and value != other_card) 
				
				this_count += 1

				
		counts[card] = this_count
		cards[:] = (value for value in cards if value != card)
		i = i + 1
		print(str(i) + " iteration(s); " + str(len(cards)) + " left")


print(counts)

with open('/home/helen/rhyme/summary.txt', 'r+') as f:
	sorted_counts = reversed(sorted(counts.items(), key = operator.itemgetter(1)))
	for card, count in sorted_counts:
		f.write(str(count) + " - " + card)

print('done')