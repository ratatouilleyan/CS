completed = False
while not completed:
    try:
        number = input("Enter a string: ")
        print(float(number))
        completed = True
    except Exception as e:
        print('exception', e)
