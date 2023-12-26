tuple = {}

tuple[(1, 2, 4)] = 8
tuple[(4, 2, 1)] = 10
tuple[(1, 2)] = 12

sum = 0
for k in tuple:
    sum += tuple[k]

print(f'{len(tuple)}+{sum}')