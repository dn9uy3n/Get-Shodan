import argparse
import shodan
import time
from configure import SHODAN_API
from django.utils.encoding import smart_str

def filter(result, filter_str, f):
    filter_list = filter_str.split('/')
    for r in result['matches']:
        tmp_str = ''
        for ft in filter_list:
            # print ft
            # print r[ft]
            try:
                if 'location' == ft[:8]:
                    lo = r['location']
                    tmp_str += smart_str(lo[ft[9:]]) + ';'
                else:
                    tmp_str += smart_str(r[ft]) + ';'
            except Exception as e:
                print(e)
                tmp_str += ';'
        f.write(tmp_str[:-1] + '\n')

def main():
    print   """  ____      _     ____  _               _             
 / ___| ___| |_  / ___|| |__   ___   __| | __ _ _ __  
| |  _ / _ \ __| \___ \| '_ \ / _ \ / _` |/ _` | '_ \ 
| |_| |  __/ |_   ___) | | | | (_) | (_| | (_| | | | |
 \____|\___|\__| |____/|_| |_|\___/ \__,_|\__,_|_| |_|\n"""

    try:
        parser = argparse.ArgumentParser(description= "get data from Shodan")
        parser.add_argument("-q", "--query", type = str, metavar = "<\'string query\'>", help = "String query search on Shodan", required=True)
        parser.add_argument("-o", "--output", type = str, metavar = "<output file>", help = "Output file", required=True)
        parser.add_argument("-f", "--filter", type = str, metavar = "ip_str/port/os/host/", help = "Filer string", required=True)
        parser.add_argument("-os", "--offset", type = int, metavar = "<offet_number>", help = "The serial number of result will begin downloading")
        parser.add_argument("-l", "--limit", type = int, metavar = "<limit_number>", help = "The number of result will download")
    except Exception:
        parser.print_help()

    args = parser.parse_args()
    query = args.query
    filter_str = args.filter
    file_str = args.output
    offset = args.offset
    limit_ = args.limit

    api = shodan.Shodan(SHODAN_API)
    result_number = api.count(query)
    total = result_number['total']

    f = open(file_str, "w")

    print ("Search query: %s has %s result" %(query, total))

    if offset > 0:
        cnt = offset
    else:
        cnt = 0

    if limit_ > 0:
        total = cnt + limit_

    check = 0

    while True:
        try:
            tmp_limit = int(total) - cnt
            if( tmp_limit < 100):
                result = api.search(query, offset = cnt, limit = tmp_limit)
                check = 0
                print "download %d/%d" %(cnt + tmp_limit,total)
                filter(result, filter_str, f)
                break
            result = api.search(query, limit=100, offset=cnt)
            check = 0
            cnt += 100
            print "download %d/%d" %(cnt,total)
            filter(result, filter_str, f)
        except shodan.exception.APIError as e:
            check += 1
            if(check > 10):
                print "Exit program after 10 time reconnection, because"
                print e
                break
            print e
            print "The program will continue for 10 seconds..."
            time.sleep(10)

    f.close()

    print("Done! :)")

main()