#!/usr/bin/python

import urllib, urllib2, json
import auth

def add(url):
	
	tokens = auth.getAuthToken()

	addUrl = 'https://getpocket.com/v3/add'
	params = {'access_token': tokens['accessKey'],
				'consumer_key': tokens['consumer_key'],
				'url': url}
	jparams = json.dumps(params)
	req = urllib2.Request(addUrl, jparams)
	req.add_header('Content-Type', 'application/json')
	response = urllib2.urlopen(req)
	
	fresp = json.loads(response.read())
	if fresp['status'] == 1:
		print 'Successfully added ' + url + ' to pocket.'
	else:
		print 'There was an error adding ' + url + ' to pocket.'



