#!/usr/bin/python

import sys
import urllib.request

RDAP_LOOPUP_URI = "https://rdap.verisign.com/com/v1/domain/"

# takes website url as argument
# prints expiration date to console
def main(argv):
    # check valid domain
    if len(argv) == 1 or (not type(argv[1]) is str):
        print("Usage: " + argv[0] + " [DOMAIN NAME] ")
        return
    website = argv[1].lower()
    # clean up url
    if website.startswith("www."):
        website = website[5:]
    # request data
    try:
        data = str(urllib.request.urlopen(RDAP_LOOPUP_URI + website).read())
        # sort data out
        lookup_str = "{\"eventAction\":\"expiration\",\"eventDate\":\""
        experiation = data.find(lookup_str)
        # check if expiration found
        if experiation == -1:
            print("Expiration was not found for " + website)
            return
        #print expiration
        print(data[experiation + len(lookup_str): experiation + len(lookup_str) + 20])
    except urllib.error.HTTPError:
        print("Domain Name not found in the registry.")

if __name__ == "__main__":
    main(sys.argv)