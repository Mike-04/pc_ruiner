def este_prim(n):
    if n in primes:
        return True
    return False

def descompunere_in_suma_prime_recursive(numar, lista_primi_partiali=[]):
    if numar == 0:
        print(lista_primi_partiali)
    for i in range(2, numar + 1):
        if este_prim(i):
            descompunere_in_suma_prime_recursive(numar - i, lista_primi_partiali + [i])

def descompunere_in_suma_prime(numar):
    stack = [(numar, [])]

    while stack:
        current_num, partial_primes = stack.pop()
        if current_num == 0:
            print(partial_primes)
        else:
            for i in range(2, current_num + 1):
                if este_prim(i):
                    stack.append((current_num - i, partial_primes + [i]))

def gen_primes(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    for i in range(int(n**0.5) + 1, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes

numar_dat = int(input("Enter a number:"))
primes=gen_primes(numar_dat)
print(primes)
print("Iterative:")
descompunere_in_suma_prime(numar_dat)
print("Recursive:")
descompunere_in_suma_prime_recursive(numar_dat)
