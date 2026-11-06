filename = input("Enter the name of the file to be written: ")

try:
    with open(filename, 'r') as f:
        content = f.read()
        content.append(440)
    with open(filename, 'w') as f:
        f.write(content)
except:
    print('nope')