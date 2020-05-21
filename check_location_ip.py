import shodan

api = shodan.Shodan('YhbjtVMFCVYvAlJ5VUwmyo7lsw6NQ2wA')

host = api.host('121.180.25.183')

print host

print "longitude: " + str(host['longitude'])
print "latitude: " + str(host['latitude'])
