import os
import shelve

def searchfile(shelvefile):

    query=input("query: ")
    query = query.split(" ")
    query = list(set(query))
    lookup = shelve.open(shelvefile)

    if ("and" in query):
        query.remove("and")
        for item in query:
            if (query[0] in lookup) and (query[1] in lookup):
                print("Found at",lookup.get(item))

    elif (("and" in query) and ("or" not in query)) or (("and" in query) and ("or" in query)) or (("or" not in query) and ("and" not in query)):
        if "and" in query:
            query.remove("and")

        if "or" in query:
            query.remove("or")
            for item in query:
                if(query[0] in lookup) or (query[1] in lookup):
                    print("Found at", lookup.get(item))
    
