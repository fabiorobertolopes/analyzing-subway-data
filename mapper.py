import sys

def mapper():
    

    for line in sys.stdin:
        data = line.strip().split(",")
        if len(data) >= 7:
            unit = data[1]
            entries = data[6]
            print "{0}\t{1}".format(unit, entries)

mapper()

