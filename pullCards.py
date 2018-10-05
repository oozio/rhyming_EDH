import urllib, urllib2
from lxml import html
import requests
import sys
import string
import re
import random
import math
import pronouncing

count = 0
colors = ['wburg','c']

with open('/home/helen/rhyme/raw.txt','r+') as f:
	for color in colors:
		url = "https://scryfall.com/search?q=commander%3A" + color 
		#url = "https://scryfall.com/search?q=commander%3A" + random.choice(colors)
		page = requests.get(url)
		tree = html.fromstring(page.content)

		card_count = int(tree.xpath('//div[@class = "search-info"]/p//text()')
			[3][1:7].replace(',',''))

		content = tree.xpath('//a[@class="card-grid-item"]/img/@title')
		content = [x[:-6] for x in content]

		#f.write(`card_count`+'\n')
		for card in content:
			f.write("%s\n" % card)

		for i in range(2, int(math.ceil(card_count / 60.0)) + 1):
			url = "https://scryfall.com/search?as=grid&order=name&page="+`i`+"&q=commander%3A"+color+"&unique=cards"

			page = requests.get(url)
			tree = html.fromstring(page.content)

			content = tree.xpath('//a[@class="card-grid-item"]/img/@title')
			content = [x[:-6] for x in content]

			for card in content:
				f.write(card.encode('utf-8') + '\n')
		
			print('done with page')
			print(i)
			print('in color')
			print(color)

			print(content)
