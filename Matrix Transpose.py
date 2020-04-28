a= int(input("Enter the numbers of row"))
b= int(input("Enter the number of columns"))
matrix=[]
#First Matrix
for i in range(a):
    c=[]
    for j in range(b):
        j=int(input("Enter the number of pocket "+str(i)+" "+str(j)+" "))
        c.append(j)
    matrix.append(c)

for i in range(a):
    for j in range(b):
        print(matrix[i][j],end=" ")
    print()

trsmat=[0,0,0],[0,0,0],[0,0,0]

for i in range(a):
    for j in range(b):
        trsmat[i][j]=matrix[j][i]

for i in range(a):
    for j in range(b):
        print(trsmat[i][j],end=" ")
    print()

