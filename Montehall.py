import random 
doors=[0]*3
goatdoor=[0]*2
swap=0;
dont_swap=0
j=1
while(j!=0):
    x=random.randint(0,2)
    doors[x]="BMW"
    for i in range(0,3):
        if(i==x):
            continue
        else:
            doors[i]="Goat"
            goatdoor.append(i)
    choice=int(input("Enter your choice"))
    door_open=random.choice(goatdoor)
    while(door_open==choice):
        door_open=random.choice(goatdoor)
    ch=input("Do you want to swap? y/n")
    if(ch=='y'):
        if(doors[choice]=='Goat'):
            print("player wins")
            swap+=1
        else:
            print("Player loose")
    else:
        if(doors[choice]=='Goat'):
            print("Player Lost")
        else:
            print("Player wins")
            dont_swap+=1
    j=int(input("Do You want to exit press 0 to exit and press 1 to continue"))

print(swap)
print(dont_swap)