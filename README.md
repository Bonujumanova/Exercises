# алгоритмические задачи

---

## coderun


* [352. Камни и украшения](./coderun/task352.py) | [Условие задачи](https://coderun.yandex.ru/problem/rocks-and-jewels/description?compiler=python)

```python 
J: str = input()
S: str = input()
count_sym = 0

for symbol in set(J):
    count_sym += S.count(symbol)

print(count_sym)


```

