#!/usr/bin/python

import sys
import urllib.request

RDAP_LOOPUP_URI = "https://rdap.verisign.com/com/v1/domain/"

# takes website url as argument
# prints expiration date to console
def main(argv):
    website = argv[1].lower()
    # TODO check for invalid characters
    if website is None or not type(website) is str:
        print("Usage: " + argv[0] + " [DOMAIN NAME] ")
    # clean up url
    if website.startswith("www."):
        website = website[5:]
    # request data
    try:
        data = urllib.request.urlopen(RDAP_LOOPUP_URI + website).read()
        print(data)
    except urllib.error.HTTPError:
        print("Domain Name not found in the registry.")

if __name__ == "__main__":
    main(sys.argv)