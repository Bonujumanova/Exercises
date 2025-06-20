J: str = input()
S: str = input()
count_sym = 0

for symbol in set(J.lower()):
    count_sym += S.lower().count(symbol)

print(count_sym)
