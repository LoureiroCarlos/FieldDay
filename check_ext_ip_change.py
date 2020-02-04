#!/usr/bin/env python
"""
Python 3.8 program that checks for changes in the public IP address
and notifies you by email (gmail) when there is a change.
If it doesn't login with the right email and pass combination please visit
this website for instructions:
https://devanswers.co/create-application-specific-password-gmail/
"""

# Imports
from requests import get
import time, smtplib, os, getpass

# Functions

# Retrieves your public IP address and assigns it to a variable
def getIp():
	try:
		ip=get('https://api.ipify.org').text
		return ip
	except:
		print("Unable to contact the IP address provider!\nPlease check your internet connection.\nNow exiting.")
		exit()

# Sends a plain text email
def sendEmail(sender_email, sender_pass, receiver_email, subject, body):
	try:
		with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
			smtp.ehlo()
			smtp.starttls()
			smtp.ehlo()
			smtp.login(sender_email, sender_pass)
			msg = f"Subject: {subject}\n\n{body}"
			smtp.sendmail(sender_email, receiver_email, msg)
	except:
		print('There was an error validating your information.\nNow exiting.')
		exit()


# Checks is the ip has changed and returns a boolean value
def checkChange(original_ip):
	ip=getIp()
	if ip==original_ip:
		return	False
	else:
		return	True

# Queries the user for the email information for sender email and receiver email
# Currently not in use
def queryUser():
	print('Please type the  email address to send the message from:')
	global sender_email
	sender_email = input('>')

	print('Please type the')
	global sender_pass
	sender_pass = getpass.getpass()
	try:
		with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
			smtp.ehlo()
			smtp.starttls()
			smtp.ehlo()
			smtp.login(sender, passw)
	except:
		print('There was an error validating your information.\nNow exiting.')
		exit()

	print('Please type the email address you wish to send the message to:')
	global receiver_email
	receiver_email = input('>')


if __name__ =='__main__':
	# retrieves the email information from the environment variables
	sender_email=os.environ.get('TER_MAIL')
	sender_pass=os.environ.get('TER_MAIL_PASS')
	receiver_email=os.environ.get('MAIL')
	# defines the time interval between checking for ip changes
	time_interval = 18000 #Time in sec.     1 hour = 3600 sec 
	orig_ip=getIp()
	# main loop
	while True:
		if checkChange(orig_ip):
			orig_ip=getIp()
			subject="YOUR PUBLIC IP ADDRESS HAS CHANGED"
			body=f"YOUR NEW IP ADDRESS IS:\n{orig_ip}"
			sendEmail(sender_email, sender_pass, receiver_email, subject, body)
			time.sleep(time_interval)
		else:
			pass
