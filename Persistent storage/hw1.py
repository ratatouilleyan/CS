import pickle, pathlib
file_path = pathlib.Path('data') / 'random_integers.ser'
integers_written = [x for x in range(6767, 6767 + 10000)]
print(integers_written[-100])

f = open(file_path, 'wb')
pickle.dump(integers_written, f)
f.close()

f = open(file_path, 'rb')
integers_read = pickle.load(f)
f.close()
print(integers_read[-100])