import shodan
from configure import SHODAN_API

api = shodan.Shodan(SHODAN_API)

host = api.host('121.180.25.183')

print host

print "longitude: " + str(host['longitude'])
print "latitude: " + str(host['latitude'])
