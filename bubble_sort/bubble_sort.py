a = [3,7,1,9,12]

print(a)
cont = 0
for j in range(len(a)-1):
    
    for i in range(len(a)-1):
        if (a[i]> a[i+1]):
            temp = a[i]
            a[i]=a[i+1]
            a[i+1]=temp
            cont+=1
            print(a)
print("ciclos =",cont)  
        
