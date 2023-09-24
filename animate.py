import turtle
# import random
turtle.bgcolor("black")
seurat = turtle.Turtle()
from random import randint

dot_distance = 25
width =5
height = 7

seurat.penup()
list_color = ["white","Yellow","brown","red","blue","green","orange","pink","violet","grey","cyan"]

#python program to print
#given matrix in spiral form

seurat.setpos(-250,250)
def spiralPrint(m,n):
    k=0
    l=0
    f=0
    
# =============================================================================
#     k = staring row index
#     m = ending row index
#     l = starting column index
#     i = iterator 
# =============================================================================
    col = randint(0,10)
    seurat.color(list_color[col])
    while(k<m and l<n):
        # print the first row from the remaininig row
        if(f==1):
            seurat.right(90)
        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
            
        k+=1
        f=1
        # print the last column from the remaining columns
        seurat.right(90)
        col = randint(0,10)
        seurat.color(list_color[col])
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
        n-=1
        
        seurat.right(90)
        col=randint(0,10)
        seurat.color(list_color[col])
        if (k<m):
            for i in range(n-1,(l-1),-1):
                seurat.dot()
                seurat.forward(dot_distance)
        m-=1
        
        seurat.right(90)
        col = randint(0,10)
        seurat.color(list_color[col])
        if(l<n):
            for i in range(m-1,k-1,-1):
                seurat.dot()
                seurat.forward(dot_distance)
            l+=1
            
    
        
            
R=20
C=20
spiralPrint(R,C)