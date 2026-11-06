import pathlib
file_path = pathlib.Path('data') / 'random_integers.txt'
if file_path.exists():
    print('reading', file_path)
else:
    #generate a random list of integers
    file_path = pathlib.Path('data') / 'random_integers.txt'
    integers_written = [x for x in range(6767, 6767 + 10000)]
    print(integers_written[-100])

    # write data onto drive with a context manager
    with open(file_path, 'w') as f:
        for i in integers_written:
            f.write(f'{i}\n')

    # read and print data from drive with a context manager
    with open(file_path) as f: # with establishes new context
        for i in f:
           print(f.read([-10]))

    # save the same list in another file
    another_file_path = pathlib.Path('data') / 'random_integers2.txt'
    with open(file_path, 'r') as f1, open(another_file_path, 'w') as f2:
        for i in f1:
            f2.write(i)

    #read from the second file and print the data
    with open(another_file_path) as f:
        print(f.read([-10]))