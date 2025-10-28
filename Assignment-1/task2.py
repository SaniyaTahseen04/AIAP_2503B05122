def is_prime(n: int) -> bool:
    """Return True if n is a prime number, otherwise False."""
    if not isinstance(n, int):
        raise TypeError("is_prime() requires an integer")
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    try:
        n = int(input("Enter an integer : ").strip())
    except ValueError:
        print("Invalid input: please enter an integer.")
    else:
        print(f"{n} is prime." if is_prime(n) else f"{n} is not prime.")