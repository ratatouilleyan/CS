def filter_file(filename_in, filename_out, cond):
    try:
        import pathlib
        file_path1 = pathlib.Path(filename_in)
        file_path2 = pathlib.Path(filename_out)
        with (open(file_path1) as f1,
              open(file_path2, 'w') as f2):
            for line in f1:
                line = line.strip()
                if line:
                    try:
                        if cond(line):
                            f2.write(line + '\n')
                    except Exception as ex:
                        print("Skipping line: ", ex)   
    except Exception as e:
        from pathlib import Path
        data_dir = Path('data')
        data_dir.mkdir(parents=True, exist_ok=True)
        print("Exception: ", e, '\n')
        if not file_path1.exists():
            file_path1.touch()
        if not file_path2.exists():
                    file_path2.touch()
        print("New files are created, try again.")

def odd(s):
    return int(s) % 2 == 1

def even(s):
    return int(s) % 2 == 0

filter_file('data/list.txt', 'data/odds.txt', odd)