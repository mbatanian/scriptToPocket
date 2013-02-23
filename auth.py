#!/usr/bin/python

import urllib, urllib2
import config

redirect_uri = 'https://github.com/mbatanian/scriptToPocket'
CONSUMER_KEY = config.getConsumerKey()

def getRequestToken():
	params = {'consumer_key': CONSUMER_KEY,
			  'redirect_uri': redirect_uri}
	reqUrl = 'https://getpocket.com/v3/oauth/request'
	encParams = urllib.urlencode(params)
	req = urllib2.Request(reqUrl, encParams)
	
	req.add_header("Content-type", "application/x-www-form-urlencoded")
	response = urllib2.urlopen(req)	

	code = response.read().split('=')[1]
	return code

def authorize():
	token = getRequestToken()
	urlForm = 'https://getpocket.com/auth/authorize?request_token={0}&redirect_uri={1}'
	url = urlForm.format(token, redirect_uri)
	print 'Please go to the following site to authorize this script:'
	print url
	authWait = raw_input('Success? (Y/N)')
	if (authWait.lower() != 'y'):
		print 'You must authorize this app on the Pocket web site to use.'
		exit(0)

	authUrl = 'https://getpocket.com/v3/oauth/authorize'
	params = {'consumer_key': CONSUMER_KEY, 'code': token }
	encParams = urllib.urlencode(params)
	req = urllib2.Request(authUrl, encParams)
	req.add_header("Content-Type", "application/x-www-form-urlencoded")
	res = {}
	try:
		response = urllib2.urlopen(req).read()
		raw = response.split('&')
		res = {'username': raw[1].split('=')[1], 'accessKey': raw[0].split('=')[1] }
	except urllib2.HTTPError, e:
		if e.code == 403:
			print 'Error authorizing account.'
		else:
			print e.code
		exit(1)
	return res

def getAuthToken(forceRefresh = False):

	if not forceRefresh:
		try:
			afile = open('accessKey.data', 'r')
			return {'accessKey': afile.read(), 'consumer_key': CONSUMER_KEY }
		except IOError as e:
			print 'accessKey file does not exist, reauthorizing...'

	authResult = authorize()
	print 'Authorized for ' + authResult['username']
	f = open('accessKey.data', 'w')
	f.write(authResult['accessKey'])
	f.close()

	return { 'accessKey': authResult['accessKey'], 'consumer_key': CONSUMER_KEY }





