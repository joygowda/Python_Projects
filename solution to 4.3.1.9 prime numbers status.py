def is_prime(num):
#
    if num ==1:
        print(f"{num} is not a prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(f"{num} is a not a prime number")
                break
        else:
            print(f"{num} is not a prime number")

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
