import socket
import sys
import time
import os
import connectify
import userlog

def check(sock):
	flag = raw_input('New User? (Y/N)')
	if flag =='Y':
		print "Create your account on http://localhost/gandharv/register.html"
		connectify.closeCon(sock)

def getUserInfo():
	username = raw_input('Enter the username')
	password = raw_input('Enter the password')
	userinfo = username+','+password
	return userinfo


def validate(sock):
	for attempt in range(0,3): 
		userinfo = getUserInfo()
		received = connectify.getResponse('1'+userinfo, sock)
		if received == '1':
			userlog.createUserlog(userinfo)
			userinfo = userinfo.split(',')[0]
			break
		else:
			print "Invalid username or password"
	if received == '0':
		print "Login Failed...Appliation Terminating..."
		connectify.closeCon(sock)
	return userinfo

def init(sock):
	check(sock)
	userinfo = validate(sock)
	return userinfo
