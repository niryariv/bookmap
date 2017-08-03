import csv
import codecs
import sys
import json

# from pymongo import MongoClient


locations = {}
with codecs.open('data/locations.csv', 'rb', encoding="iso8859-8") as csvfile:
    data = csv.reader(csvfile)
    for r in data:
        name = r[3].strip()
        latlng = (float(r[5]), float(r[6]))
        locations[name] = latlng
        # print (name)

# print (locations)
# exit()

books = {}
c = 0
with codecs.open('data/books.csv', 'rb', encoding="iso8859-8", errors="replace") as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        # c+=1
        # if c > 100:
        #     break

        # not all books have known locations
        loc  = row['X924'].strip()
        if loc not in locations.keys():
            continue
        latlng = locations[loc]

        y = row['X008year1']
        if not y.strip().isdigit():
            continue

        year = int(y)
        if year > 2017:
            continue
            
        if year in books.keys():
            books[year].append(latlng)
        else:
            books[year] = [latlng]


# print (books)
# print ("==========")
out = json.dumps(books)
print (out)

# print(books)
# print(len(books))
