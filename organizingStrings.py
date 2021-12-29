import itertools
File = [l.strip() for l in open('rosalind_lexf.txt', 'r').readlines()]

collection = File[0]
n = int(File[1])
symbols = ''.join(symbol for symbol in collection if symbol != ' ')
res = symbols
for i in range(n-1):
    res = list(itertools.product(res, symbols))

    temp_res = []
    for item in res:
        temp_res.append(item[0] + item[1])
    res = temp_res

for symbol in res:
    print(symbol)