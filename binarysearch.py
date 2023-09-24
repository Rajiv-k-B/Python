


def linear_search(s,n,x):
    element=[]
    for i in range(s,n):
        element.append(i)
    
    flag=0
    for i in element:
        if(i==x):
            print("Yes !! I found my number at position : "+str(i))
            flag=1
    if(flag==0):
        print("Number is not found")
        
        

def binary_search(a,x):
    first_pos=0
    last_pos=len(a)-1
    flag=0
    count = 0
    while(first_pos<last_pos and flag==0):
        mid=(first_pos+last_pos)//2
        if(x==a[mid]):
            flag=1
            print("The element is present st pos: "+str(mid))
            print("The number of iterations are: "+str(count))
            return
        else:
            if(x<a[mid]):
                last_pos=mid-1
            else:
                first_pos=mid+1
    print("The number is not present")
    
    
a=[]
for i in range (1,1001):
    a.append(i)
    
binary_search(a, 1000)