# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:06:56 2020

@author: Akarsh
"""
import turtle
# changing the background color of the screen
turtle.bgcolor("black")

seurat= turtle.Turtle()
from random import randint
# Distance
dot_distance=25
# Pointer size
wigth= 5
height= 7

seurat.penup()
list_color=["white","yellow","brown","red","blue","green","orange","pink","violet","grey","cyan"]

# Position of pointer
seurat.setpos(-250,250)

'''
# Number
def spiral(r,c,m):
'''
# For turtle
def spiral(r,c):
    k=0
    l=0
    flag=0
    
    col=randint(0,10)
    seurat.color(list_color[col])
    
    while(k<r and l<c):
        
        if(flag==1):
            seurat.right(90)
        # Printing the first row
        for i in range(l,c):
            seurat.dot()
            seurat.forward(dot_distance)
            # print(m[k][i] ,end=" ")
            
        k+=1
        flag=1
        
        seurat.right(90)
        
        col=randint(0,10)
        seurat.color(list_color[col])
        
        # Printig the last column
        for i in range(k,r):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(m[i][c-1], end=" ")
         
        c-=1 
        
        seurat.right(90)
        
        col=randint(0,10)
        seurat.color(list_color[col])
        if(k<r):
            # Printing the last row
            for i in range(c-1, l-1, -1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(m[r-1][i], end=" ")
            
            r-=1
        seurat.right(90)
        col=randint(0,10)
        seurat.color(list_color[col])
        if(l<c):
            # Printing the first column
            for i in range(r-1, k-1, -1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(m[i][l],end=" ")
            l+=1    
 

# For printing in turtle
            
spiral(20,20)
turtle.done()            

# For printing in number
'''           
m=[]
count = 1
n=int(input("Enter the matrix number"))
for i in range(n):
    l=[]
    for j in range(n):
        l.append(count)
        count+=1
    m.append(l)
spiral(n,n,m)    
'''            

