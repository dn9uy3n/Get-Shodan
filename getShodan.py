import argparse
import shodan

def filter(result, filter_str, f):
    filter_list = filter_str.split('/')
    for r in result['matches']:
        tmp_str = ''
        for ft in filter_list:
            # print ft
            # print r[ft]
            tmp_str += ft + ' ' + str(r[ft]) + ';'
        f.write(tmp_str + '\n')

def main():
    parser = argparse.ArgumentParser(description= "get data from Shodan")
    parser.add_argument("-q", "--query", type = str, metavar = "<\'string query\'>", help = "String query search on Shodan")
    parser.add_argument("-k", "--key", type = str, metavar = "<shodan_API_key>", help = "API key in Shodan")
    parser.add_argument("-o", "--output", type = str, metavar= "<output file>", help = "Output file")
    parser.add_argument("-f", "--filter", type = str, metavar= "ip_str/port/os/host/", help = "filer string")

    args = parser.parse_args()
    query = args.query
    key = args.key
    filter_str = args.filter
    file_str = args.output

    api = shodan.Shodan(key)

    result_number = api.count(query)

    print file_str

    f = open(file_str, "w")

    print ("Search query: %s has %s result" %(query, result_number['total']))

    cnt = 0

    while True:
        tmp_limit = int(result_number['total']) - cnt
        if( tmp_limit < 10000):
            result = api.search(query, offset = cnt, limit = tmp_limit)
            filter(result, filter_str, f)
            print "hanle %d/%d" %(cnt + tmp_limit,result_number['total'])
            break
        result = api.search(query, limit=10000, offset=cnt)
        filter(result, filter_str, f)
        cnt += 10000
        print "hanle %d/%d" %(cnt,result_number['total'])
    
    f.close()

    print("Done! :)")

main()