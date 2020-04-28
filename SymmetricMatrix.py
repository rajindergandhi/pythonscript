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

trnsmat=[0,0,0],[0,0,0],[0,0,0]

for i in range(a):
    for j in range(b):
        trnsmat[i][j]=matrix[j][i]
    print()

for i in range(a):
    for j in range(b):
        print(trnsmat[i][j],end=" ")
    print()

f=0
for i in range(a):
    for j in range(b):
        if matrix[i][j]!=trnsmat[i][j]:
            f=1
            break

if f==0:
    print("Matrix is symmetric")
else:
    print("matrix is not symmetric")
