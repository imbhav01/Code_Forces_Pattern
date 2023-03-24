x = str(input()).split()
y = str(input())
z = []

for i in range(0,len(y)):
    z.append(y[i])

for i in range(0,int(x[1])):
    for j in range(1,int(x[0])):
        if z[j]=="G" and z[j-1]=="B":
                    z[j]="B"
                    z[j-1]="G"
                
            
            
print(z)