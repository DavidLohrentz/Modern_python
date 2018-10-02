numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\nnumbers are {numbers}")
evens = [x for x in numbers if x % 2 == 0]
print(f"\nevens are {evens}")
odds = [y for y in numbers if y % 2 == 1]
print(f"\nodds are {odds}\n")
