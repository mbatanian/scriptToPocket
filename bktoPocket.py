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
def traverse(root, folder):
	for x in root['children']:
		if (x['name'] == folder) and (x['type'] == 'folder'):
			return x
		elif x['type'] == 'folder':
			p = traverse(x, folder)
			if p != 'Not found':
				return p
	return 'Not found'


def findFolder(folder):
	bkfile = open(config.getBookmarkFileLocation(), 'r')
	bks = json.loads(bkfile.read())
	return traverse(bks['roots']['bookmark_bar'], folder)


def getItem(folder):

	sourceFolder = findFolder(folder)
	if sourceFolder == 'Not found':
		print 'Could not find folder ' + folder
		exit(0)

	items = sourceFolder['children']

	while True:
		if len(items) == 0:
			print 'No items found in folder ' + folder
			exit(0)
		id = random.randint(0, len(items)-1)
		article = items[id]
		# don't return folders for now
		if article['type'] == 'url':
			return article

toSave = getItem(config.getBookmarkFolder())

url = toSave['url']
name = toSave['name']

print 'Saving ' + name + ' to pocket'
pocket.add(url)
