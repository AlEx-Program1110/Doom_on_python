from setting_variables import *
text_map = [
    'BBBBBBBBBBBBBBBBB',
    'B................B',
    'B..B....B...BBBBBB',
    'B..BB............B',
    'B...........BBBBBB',
    'B....B.B....B',
    'B...........B',
    'BBBBBBBBBBBB',
]
map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            map.add((i * TITLE, j * TITLE))
