J: str = input()
S: str = input()
count_sym = 0

for symbol in set(J):
    count_sym += S.count(symbol)

print(count_sym)
