#!/usr/bin/python

import urllib, urllib2, json
import auth

def add(url, tags = []):
	
	tokens = auth.getAuthToken()

	addUrl = 'https://getpocket.com/v3/add'
	params = {'access_token': tokens['accessKey'],
				'consumer_key': tokens['consumer_key'],
				'url': url}

	if len(tags) > 0:
		params['tags'] = ','.join(tags)

	jparams = json.dumps(params)
	req = urllib2.Request(addUrl, jparams)
	req.add_header('Content-Type', 'application/json')
	try: 
		response = urllib2.urlopen(req)
	except urllib2.HTTPError, e:
		if e.code == 400:
			print 'Error saving'
			print 'Please ensure you used the fully qualified url'
			print ' (i.e. https://www.google.com instead of www.google.com)'
			return
		else:
			raise

	fresp = json.loads(response.read())
	if fresp['status'] == 1:
		print 'Successfully added ' + url + ' to pocket.'
	else:
		print 'There was an error adding ' + url + ' to pocket.'



