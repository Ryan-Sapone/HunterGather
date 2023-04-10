# HunterGather
An OSINT tool used for searching first/last names, email addresses, usernames, phone numbers, and domains. This script makes use of hardcoded web URLs from well known OSINT websites as well as tools like Sherlock, Phoneinfoga, Subfinder, Assetfinder, Amass, HTTProbe, and GoWitness. This does not use any API keys, so the script will instead provide hyperlinks that you can use to help speed up your OSINT gathering. This also has the benefit of not interacting with these websites until you click the link, so there shouldn't be issues with rate limiting or captchas. Some of the provided links do however require manual intervention, and the script will note that.

# Requirements
The only requirement is to install argparse, which can be done with the following command: `pip3 install argparse` (or just `pip install argparse` if you only have Python 3). Make sure to also give execute permissions with `chmod +x HunterGather.py`

# How To Use
Once the script is on your system, you can type `-h` or `--help` to see the arguments. These include:
- `-n` or `--name`: requires a first and last name | Ex: `./HunterGather.py -n george washington`
- `-e` or `--email`: requires a full email address | Ex: `./HunterGather.py -e george.washington1776@gmail.com`
- `-u` or `--username`: requires an online username | Ex: `./HunterGather.py -u xxgeorgewash1776xx`
- `-p` or `--phone`: requires a 10 digit phone number without any spaces or special characters | Ex: `./HunterGather.py -p 1234567890`
- `-d` or `--domain`: requires a FQDN | Ex: `./HunterGather.py -d georgewashington.org`
- `-f` or `--fast`: only useful for phone and username searches, this flag will skip running Phoneinfoga and Sherlock (the script will still be usable if you do not have these installed, no need for the flag)
- `-F` or `--FAST`: only useful for domain searches, this flag will skip running Subfinder, Assetfinder, Amass, HTTProbe, and GoWitness (the script will still be usable if you do not have these installed, no need for the flag)

# Optional
Once this tool is installed, you can add it to your PATH so that it's usable from any directory. This is recommended because any output created from the domain searches will be saved inside of your current directory, so you can make a directory specifically for each domain you're looking at and run this program from there. You can move this to your PATH by executing `sudo mv HunterGather.py /usr/local/bin/HunterGather`

# Examples
![Help Page](https://user-images.githubusercontent.com/107446796/230802792-91d1b299-0db5-477b-92e4-c4ac02349f7a.png)

![Ex1](https://user-images.githubusercontent.com/107446796/230802807-ea2c3552-534e-4802-b6a8-3e8839767b3a.png)

![Ex2](https://user-images.githubusercontent.com/107446796/230802819-7be10fba-2be9-4f29-8bd9-b75a59549028.png)
