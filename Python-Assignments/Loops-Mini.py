#program for printing pascal triangle up to 'n' rows

n = int (input ("Enter your value : "))

for i in range(n):
    
    print(' '*(n-i), end='')
 
    
    print(' '.join(map(str, str(11**i))))

print("\n")

#program for printing pattern

#dimond

rows_dimond = 9
print("Dimond")
for i in range(1, (rows_dimond+1)//2 + 1): 
    for j in range((rows_dimond+1)//2 - i):
        print(" ", end = "")
    for k in range((i*2)-1):
        print("*", end = "")
    print()

for i in range((rows_dimond+1)//2 + 1, rows_dimond + 1): 
    for j in range(i - (rows_dimond+1)//2):
        print(" ", end = "")
    for k in range((rows_dimond+1 - i)*2 - 1):
        print("*", end = "")
    print()

print("\n")

#triangle

rows_triangle = 5
print("Trinagle")
for i in range(rows_triangle):
    for j in range(rows_triangle-i):
        print(' ', end='')     
    for j in range(2*i+1):
        if j==0 or j==2*i or i==rows_triangle-1:
            print('*',end='')
        else:
            print(' ', end='')
    print()
    
print("\n")

#90 degree triangle upside down

rows_tri90= 5
print("90 Degree Triangle")
for i in range(1, rows_tri90+1):
    for j in range(1, rows_tri90+1):
        if (j == rows_tri90) or (i == 1) or (j == i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


 






    



    
