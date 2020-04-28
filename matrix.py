a= int(input("Enter the numbers of row"))
b= int(input("Enter the number of columns"))
matrix1=[]
#First Matrix
for i in range(a):
    c=[]
    for j in range(b):
        j=int(input("Enter the number of pocket "+str(i)+" "+str(j)+" "))
        c.append(j)
    matrix1.append(c)

#Second Matrix
matrix2=[]
for i in range(a):
    d=[]
    for j in range(b):
        j=int(input("Enter the number of pocket "+str(i)+" "+str(j)+" "))
        d.append(j)
    matrix2.append(d)


for i in range(a):
    for j in range(b):
        print(matrix1[i][j],end=" ")

    print()
for i in range(a):
    for j in range(b):
        print(matrix2[i][j],end=" ")
    print()

result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(a):
    for j in range(b):
        result[i][j]= matrix1[i][j] * matrix2[i][j]


for i in range (a):
    for j in range(b):
        print(result[i][j],end=" ")
    print()

