m = int(input("Input m rows "))
n = int(input("Input n columns "))
for i in range(m):
    s = "" # for one line
    for j in range(n):
        if i == 0 or i == m-1 or j == 0 or j == n-1:
            s += "* "
        else:
            s += "  "
    print(s)

         
        
        

