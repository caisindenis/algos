def generate_primes(n):
    if n < 2:
        return []
    size = (n - 3) // 2 + 1
    primes = [2]
    is_prime = [True] * size
    for i in range(size):
        p = i * 2 + 3
        primes.append(p)
        for j in range(2 * i**2 + 6 * i + 3, size, p):
            is_prime[j] = False
    return primes
