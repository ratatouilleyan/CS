import pathlib
file_path = pathlib.Path('data') / 'points.txt'
with open(file_path) as f: # with establishes new context
    for line in f:
        print(line, end='')
# context closes, file closed automatically