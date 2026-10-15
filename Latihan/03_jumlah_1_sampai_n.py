def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

for n in [1, 5, 10, 100]:
    rumus = n * (n + 1) // 2
    print(f"n={n} | Fungsi: {jumlah_n(n)} | Rumus n(n+1)/2: {rumus}")