#!/usr/bin/python

import json, random
import pocket, config

# Grab a file from a folder in the Chrome Bookmarks, save it to pocket

# Bookmark hierarchy explanation
# -----------
# 'roots' : top level of Bookmarks
# 'bookmark_bar': items in the bookmark_bar
# 'children': Actual Bookmarks inside the bookmark bookmark_bar
# [0]: First item in the bookmark_bar
# children: children of that item ('it's a folder)
# ... and so on
def getItem():

	bkfile = open(config.getBookmarkFileLocation(), 'r')
	bks = json.loads(bkfile.read())

	sourceFolder = bks['roots']['bookmark_bar']['children'][0]['children'][0]
	items = sourceFolder['children']

	while True:
		id = random.randint(0, len(items)-1)
		article = items[id]
		# don't return folders for now
		if article['type'] == 'url':
			return article

toSave = getItem()

url = toSave['url']
name = toSave['name']

print 'Saving ' + name + ' to pocket'
pocket.add(url)