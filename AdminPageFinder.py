#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("link.txt","r");
	link = raw_input("Enter Site Name \n(example ==> target.com or www.target.com ): ")
	print "\n\nScanning Progress............. \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link

def Credit():
	Space(10); print "#####################################"
	Space(10); print "#        Admin Page Finder          #"
	Space(10); print "#      Tools by AbraKdabra          #"
	Space(10); print "#    Indonesian Ethical Hacking     #"
	Space(10); print "#####################################"

Credit()
findAdmin()
