def csv_reader(path):
    with open(path) as csv_file:
        for row in csv_file:
            lst = row.strip().split(',')
            new = sum(map(int, lst))
            lst.append(' ' + str(new))
            yield ','.join(lst)

def process(path):
    lines = csv_reader(path)
    with open('ans.csv', 'w') as out:
        for line in lines:
            out.write(line + '\n')
