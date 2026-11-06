try:
    import pathlib
    filename = input("Enter a filename: ")
    file_path =  pathlib.Path(__file__).resolve().parent / "data" / filename
    with open(file_path) as f:
        numbers = [int(line) for line in f if line.strip()]
        print(sum(numbers) / len(numbers))
except Exception as e:
    print("exception:", e)