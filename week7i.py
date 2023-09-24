# =============================================================================
# def spiral(row, column, arr):
#     rowStart = 0;
#     columnStart=0;
#     while(rowStart<row and columnStart<column):
#         for i in range(rowStart,row):
#             print(arr[i][columnStart], end=" ")
#         columnStart = columnStart+1
#         for i in range (columnStart, column):
#             print(arr[row-1][i], end=" ")
#         row = row-1
#         
#         if(rowStart<row):
#             for i in range(row-1, rowStart-1,-1):
#                 print(arr[i][column-1], end = " ")
#             column = column-1
#         if(columnStart<column):
#             for i in range(column-1, columnStart - 1, -1):
#                 print(arr[rowStart][i], end=" ")
#             rowStart=rowStart+1
# matrix=[[1,2,3],[5,6,7],[9,10,11]]
# 
# row=3
# column=3
# 
# spiral(row,column,matrix)
# =============================================================================
# =============================================================================
# import turtle
# 
# pen = turtle.Turtle()
# 
# for i in range(6):
#     pen.right(60)
#     pen.forward(60)
# 
# turtle.done()
# =============================================================================

# =============================================================================
# def sum(arr,n):
#     sum=0
#     sum1=0
#     for i in range(n):
#         for j in range(n):
#             if(i==j):
#                 sum = sum+arr[i][j]
#             if ((i+j)==(n-1)):
#                 sum1=sum1+arr[i][j]
#     print(sum)
#     print(sum1)     
# a=[[1,2,3],[4,5,6],[7,8,9]]
# 
# sum(a,3)
# =============================================================================


import turtle
pen = turtle.Turtle()

for i in range(3):
    pen.right(60)
    pen.forward(60)
    pen.right(60)
    pen.forward(60)

turtle.done()
