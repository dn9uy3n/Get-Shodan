# Get-Shodan
The program allows to download large data from shodan quickly, simply and avoid errors.

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
  -k <shodan_API_key>, --key <shodan_API_key>
                        API key in Shodan
  -o <output file>, --output <output file>
                        Output file
  -f ip_str/port/os/host/, --filter ip_str/port/os/host/
                        Filer string
  -os <offet_number>, --offset <offet_number>
                        The serial number of result will begin downloading
  -l <limit_number>, --limit <limit_number>
                        The number of result will download

```

### 1. Install:
