def reducer():
    entriesTotal = 0
    oldKey = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            continue
        
        thisKey, thisEntry = data_mapped
        
        try:
            thisEntry_to_f = float(thisEntry)
            if oldKey and oldKey != thisKey:
                print "{0}\t{1}".format(oldKey, entriesTotal)
                oldKey = thisKey
                entriesTotal = 0
            
            oldKey = thisKey
            entriesTotal += thisEntry_to_f
        except ValueError:
            pass

reducer()
