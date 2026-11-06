class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

try: #avoid program crash by handling exceptions
    import pathlib
    #file_path = pathlib.Path('data') / 'numbers.txt'
    file_path = pathlib.Path(__file__).resolve().parent / 'data' / 'numbers.txt'
    with open(file_path) as f:
        points_read = []
        for line in f: # traverse lines
            # extract x, y
            [x, y] = [int(word) for word in line.split()]
            points_read.append(Point(x, y))
    print(points_read[-1])
except Exception as e: # handle any exception raised
    print('exception:', e)