#!/bin/python3
# Version 1.0 created by HotelSix on 2023-04-08 18:34

import sys
import argparse
import subprocess

# Defining colors for result output
RED = "\033[31m"
RESET = "\033[0m"

# Defining wrapper
def Wrapper():
	print(f"{RED}{'-' * 60}{RESET}")

# Defining arguments for the script
parser = argparse.ArgumentParser(description="An OSINT script for providing links for OSINT gathering")
parser.add_argument('-n', '--name', nargs=2, type=str, help='Enter a first name and last name separated by a space')
parser.add_argument('-e', '--email', nargs=1, type=str, help='Enter a full email address')
parser.add_argument('-u', '--username', nargs=1, type=str, help='Enter a username')
parser.add_argument('-p', '--phone', nargs=1, type=int, help='Enter a 10 digit phone number with no spaces or characters')
parser.add_argument('-f', '--fast', action='store_true', help='Skips Phoneinfoga and Sherlock lookups for phone and username searches')
args = parser.parse_args()

# Functions based on arguments
def NameLookup():
	print(" " * 20 + "SEARCHING FOR NAME" + " " * 20)
	Wrapper()
	first_name = args.name[0].capitalize()
	last_name = args.name[1].capitalize()
	print(f"Results for name: {first_name} {last_name}")
	print(f"{RED}Google: {RESET}https://www.google.com/search?q=%22{first_name}+{last_name}%22")
	print(f"{RED}Search People Free: {RESET}https://www.searchpeoplefree.com/find/{first_name}-{last_name}")
	print(f"{RED}White Pages: {RESET}https://www.whitepages.com/name/{first_name}-{last_name}?fs=1&searchedName={first_name}%20{last_name}")
	print(f"{RED}True People Search: {RESET}https://www.truepeoplesearch.com/results?name={first_name}%20{last_name}")
	print(f"{RED}Fast People Search: {RESET}https://www.fastpeoplesearch.com/name/{first_name}-{last_name}")
	print(f"{RED}Webmii: {RESET}https://webmii.com/people?n=%22{first_name}%20{last_name}%22#gsc.tab=0&gsc.q=%22{first_name}%20{last_name}%22&gsc.sort=date")
	print(f"{RED}Voter Records: {RESET}https://voterrecords.com/voters/{first_name}-{last_name}/1")
	Wrapper()
	print("\n")
def EmailLookup():
	print(" " * 20 + "SEARCHING FOR EMAIL" + " " * 20)
	Wrapper()
	email = args.email[0]
	user, domain = email.split("@")
	print(f"Results for email: {email}")
	print(f"{RED}Google: {RESET}https://www.google.com/search?q=%22{user}%40{domain}%22")
	print(" * May require manual input for verification * ")
	print(f"{RED}*Email Hippo: {RESET}https://tools.emailhippo.com/")
	print(f"{RED}*Email Checker: {RESET}https://email-checker.net/")
	Wrapper()
	print("\n")
def UsernameLookup():
	print(" " * 20 + "SEARCHING FOR USERNAME" + " " * 20)
	Wrapper()
	username = args.username[0]
	print(f"Results for username: {username}")
	print(f"{RED}Google: {RESET}https://www.google.com/search?q=%22{username}%22")
	print(" * May require manual input for verification * ")
	print(f"{RED}*Namechk: {RESET}https://namechk.com/namechk-plugin-search-results/?n={username}")
	print(f"{RED}*Name Checkup: {RESET}https://namecheckup.com/")
	print(f"{RED}*WhatsMyName: {RESET}https://whatsmyname.app/")
	if not args.fast:
		print(f"{RED}Running Sherlock...{RESET}")
		try:
			sherlock_command = f"sherlock {username}"
			output = subprocess.check_output(sherlock_command, shell=True)
			print(output.decode())
			try:
				filename = f"{username}.txt"
				subprocess.run(["rm", filename])
			except:
				print(f"Sherlock output saved to {username}.txt")
		except:
			print("Sherlock not found, skipping!")
	Wrapper()
	print("\n")
def PhoneLookup():
	print(" " * 20 + "SEARCHING FOR PHONE NUMBER" + " " * 20)
	Wrapper()
	phone = args.phone[0]
	print(f"Phone: {phone}")
	print(f"{RED}Google: {RESET}https://www.google.com/search?q=%22{phone}%22")
	print(f" * May require manual input for verification * ")
	print(f"{RED}*Caller ID Test: {RESET}https://calleridtest.com/")
	print(f"{RED}*Infobel: {RESET}https://www.us-info.com/en/usa")
	if not args.fast:
		print(f"{RED}Running Phoneinfoga...{RESET}")
		try:
			phoneinfoga_command = f"phoneinfoga scan -n {phone}"
			output = subprocess.check_output(phoneinfoga_command, shell=True)
			print(output.decode())
		except:
			print("Phoneinfoga not found, skipping!")
	Wrapper()
	print("\n")
	
# Checking for arguments 
print("\n")
if args.name:
	NameLookup()
if args.email:
	EmailLookup()
if args.username:
	UsernameLookup()
if args.phone:
	PhoneLookup()
