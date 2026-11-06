completed = False

while not completed:
    try:
        filename = input("please give filename: ")
        with open(filename,'at') as f: # 'at' append to the end of the file
            print(440, file = f)
        completed = True
    except Exception as e:
        print('exception:', e)
