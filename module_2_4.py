numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for number in numbers:
    prime = True
    if number == 1:
        continue
    else:
        for delitel in range(2, number):
            if number % delitel == 0:
                  prime = False
                  not_primes.append(number)
                  break
        if prime:
            primes.append(number)
print(f"Список простых чисел: {primes}")
print(f"Список не простых чисел: {not_primes}")