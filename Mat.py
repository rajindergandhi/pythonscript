a= int(input("Enter the numbers of row"))
b= int(input("Enter the number of columns"))
matrix=[]

for i in range(a):
    c=[]
    for j in range(b):
        j=int(input("Enter the number of pocket "+str(i)+" "+str(j)+" "))
        c.append(j)
    print()
    matrix.append(c)

for i in range(a):
    for j in range(b):
        print(matrix[i][j],end=" ")
    print()