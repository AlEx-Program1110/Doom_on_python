from setting_variables import *
text_map = [
    'BBBBBBBBBBBB',
    'B..........B',
    'B..B....B..B',
    'B..BB......B',
    'B..........B',
    'B....B.B...B',
    'B..........B',
    'BBBBBBBBBBBB',
]
map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == BLOCK_CHAR:
            map.add((i * TITLE, j * TITLE))
