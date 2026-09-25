n = int(input('Nhap n: '))
divisor_sum = 0
for i in range(1,n):
    if n % i == 0:
        divisor_sum += i
if divisor_sum == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is NOT perfect number")
    
    

