#!/usr/bin/python

import sys, urllib2, re
import pocket

def getCurrentIssueURL():

	# get the main page
	harpersUrl = 'http://www.harpers.org'
	req = urllib2.Request(harpersUrl)
	response = urllib2.urlopen(req)
	resp =  response.read()

	# terrible HTML regex parsing, ahoy!
	ciMatchString = '<li class="curentIssue"><a href="(.*)">'
	return re.search(ciMatchString, resp).groups()[0]

def addItems():
	url = getCurrentIssueURL()
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	resp = response.read()
	
	matchString = '<a href="'+url+'.*/">'	
	for x in set(re.findall(matchString, resp)):
		url = x.split('"')[1] + '?single=1'
		pocket.add(url)