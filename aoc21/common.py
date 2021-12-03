def get_int_input(day):
    file_name = f'input{str(day).zfill(2)}.txt'
    with open(f'./inputs/{file_name}') as fh:
        return [int(i) for i in fh.read().splitlines()]

