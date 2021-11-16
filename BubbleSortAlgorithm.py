a = [7, 5, -8, 0, 10, 1]
N = len(a)
for i in range(0, N - 1):
    for j in range(0, N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)