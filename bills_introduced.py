# Useful for getting data into correct format for treemaps
from helper import createLevel
import csv, json

# Example usage:
legsCsv = csv.reader(open('bills_introduced.csv', 'rU'))

# CSV header columns
LEG_ID = 0
FULL_NAME = 1
CHAMBER = 2
DISTRICT = 3
PARTY = 4
BILLS_INTRODUCED = 5
BIO_PAGE = 6
PHOTO_URL = 7

senateChildren = []
houseChildren = []

for leg in legsCsv:
    data = {'district': leg[DISTRICT], 'party': leg[PARTY], 'chamber': leg[CHAMBER], 'bills_introduced': leg[BILLS_INTRODUCED], 'full_name': leg[FULL_NAME], 'photo_url': leg[PHOTO_URL],}
    name = leg[FULL_NAME]
    area = leg[BILLS_INTRODUCED]
    color = '#CCC'
    if leg[CHAMBER] == 'Senate':
        senateChildren.append(createLevel(name, leg[FULL_NAME], area, color, data=data))
    elif leg[CHAMBER] == 'House':
        houseChildren.append(createLevel(name, leg[FULL_NAME], area, color, data=data))

senate = createLevel('Senate', 'senate', 20, '#FFF', children=senateChildren);
house = createLevel('House', 'house', 20, '#FFF', children=houseChildren);

root = createLevel('Minnesota\'s First-Term Legislators', 'root', 20, '#FFF', children=[senate, house])

print json.dumps(root, indent=4)
out = open('bills_introduced.json', 'wb')
out.write(json.dumps(root))