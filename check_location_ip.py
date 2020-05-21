import shodan
from configure import SHODAN_API
import argparse
import sys

def main():
    api = shodan.Shodan(SHODAN_API)

    host = api.host(str(sys.argv[1]))

    print host

    print "longitude: " + str(host['longitude'])
    print "latitude: " + str(host['latitude'])

    print "Google maps: https://maps.google.com/?q=<" + str(host['longitude']) + ">,<" + str(host['latitude']) + ">"