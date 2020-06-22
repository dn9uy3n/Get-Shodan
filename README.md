# Get-Shodan

Shodan is a search engine that lets the user find specific types of computers (webcams, routers, servers, etc.) connected to the internet using a variety of filters. Some have also described it as a search engine of service banners, which are metadata that the server sends back to the client.[1] This can be information about the server software, what options the service supports, a welcome message or anything else that the client can find out before interacting with the server. (wikipedia)

Downloading data in the usual way from shodan will have some difficulties such as:
 - Excessive download data (you must refine the necessary data from the json string list)
 - Disconnect during download
 - Long wait time
 
This tool will help you fix all that

```
root@kali:~/getShodan# python getShodan.py -h
  ____      _     ____  _               _             
 / ___| ___| |_  / ___|| |__   ___   __| | __ _ _ __  
| |  _ / _ \ __| \___ \| '_ \ / _ \ / _` |/ _` | '_ \ 
| |_| |  __/ |_   ___) | | | | (_) | (_| | (_| | | | |
 \____|\___|\__| |____/|_| |_|\___/ \__,_|\__,_|_| |_|

usage: getShodan.py [-h] -q <'string query'> -k <shodan_API_key> -o <output
                    file> -f ip_str/port/os/host/ [-os <offet_number>]
                    [-l <limit_number>]

get data from Shodan

optional arguments:
  -h, --help            show this help message and exit
  -q <'string query'>, --query <'string query'>
                        String query search on Shodan
  -o <output file>, --output <output file>
                        Output file
  -f ip_str/port/os/host/, --filter ip_str/port/os/host/
                        Filer string
  -os <offet_number>, --offset <offet_number>
                        The serial number of result will begin downloading
  -l <limit_number>, --limit <limit_number>
                        The number of result will download

```

The options in --filter are saved in options.txt file.
The Shodan country codes are saved in countries.txt file.

### 1. Install & Prepare:
Install the library package:

```
root@kali:~# pip install -r requitements.txt
```
Download tool:

```
root@kali:~# git clone https://github.com/dn9uy3n/Get-Shodan
```

Get Shodan API key: Login to https://www.shodan.io >> 'My Account' >> Copy API Key
Add Shodan API key to configure.py file


'''
...
SHODAN_API = <your_API_key>
...

```
...
SHODAN_API = <your_API_key>
...
```


### 2. Run:
Example: Download IP list of Apache server opens port 8080 and OS: Windows Server 2003. Save in out.txt

```
root@kali:~# python getShodan.py -q 'apache port:"8080" os:"Windows Server 2003"' -o out.txt -f ip_str
```

Open out.txt file:
```
116.211.11.111
173.239.37.150
136.142.245.117
89.31.96.48
60.248.227.26
...
```

### 3. Get location from IP:
Get the resulting IP location from shodan:



```

$ python check_location_ip.py 91.177.226.21
...
longitude: 4.3337
latitude: 50.8336
Google maps: https://maps.google.com/?q=50.8336,4.3337


```
