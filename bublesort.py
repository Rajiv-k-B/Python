
def bubble(a):
    n=len(a)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                
a=[5,4,3,1,9,0,6]
bubble(a)

for i in range(len(a)):
    print(a[i])