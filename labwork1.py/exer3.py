n = int(input('Nhap n: '))
is_prime = True

if n<= 1:
    is_prime = False
else:
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break;
if is_prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is NOT prime number")
    
    

    