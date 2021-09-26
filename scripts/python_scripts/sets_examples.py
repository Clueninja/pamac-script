A = set(x for x in range(100))
B = set(x for x in range(1000))
A.update(B)
print(A)