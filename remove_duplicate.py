#/bin/python2
import sys


def main():
    if (len(sys.argv) != 3):
        print('remove_duplicate.py input_file output_file')
    else:
        lines_seen = set() # holds lines already seen
        with open(sys.argv[2], "w") as output_file:
            for each_line in open(sys.argv[1], "r"):
                if each_line not in lines_seen: # check if line is not duplicate
                    output_file.write(each_line)
                    lines_seen.add(each_line)


main()