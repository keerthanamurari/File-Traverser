import os
import pickle
import shelve


def indexer_data(shelvefile,picklefile):

    file=open(picklefile, "br")
    flist = pickle.load(file)
    fdict = {}

    for ftuple in flist:
        flist_enum = list(ftuple[1:])
        for fsent_enum in flist_enum:
            fwords_enum = fsent_enum.split()
            for fword_enum in fwords_enum:
                fdict.setdefault(fword_enum,[]).append(ftuple[0:1])

    s = shelve.open(shelvefile)
    for key,value in fdict.items():
        s[key]=(value)

    file.close
    s.close()

    
