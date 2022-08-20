import numpy as np
from matplotlib import pyplot as plt
import math
import time 

#************************************#

#setting up domain scales
x_length = 100 
"""length of domain"""
y_length = 100  
"""height of domain"""
AR = 2         
"""aspect ratio= x_length/y_length"""
ew = 1         
"""element_width(m)"""
eh = ew*AR     
"""element height(m)"""



#************************************#

#setting up solution parameters
it=0
iterations = 108       
"""number of iterations"""
error_acquired = 0            
"""obtained during calculation"""
error_limit = 10**(-6)   
"""Stop condition: Below this limit""" 

#************************************#

#setting up velocity arrays

u_ct = np.zeros((y_length + 2, x_length + 2)) 
"""Current time, generating a matrix with zero veocity at all nodes
including boundaries, and ghost cells are stacked on top and bottom.
containing data at a time t."""

u_nt = np.zeros((y_length + 2,x_length + 2))
"""Current time + 1, generating a matrix with zero veocity at all nodes
including boundaries, and ghost cells are stacked on top and bottom.
lcontaining data at a time t+1."""

    #"""Checking the output of the u_ct and u_nt"""
    #print ("u_ct", u_ct.shape)
    #print ("\nu_nt", u_nt.shape)
     
#************************************#

#setting up mesh

"""For the Current time: ghost cells set-up"""
u_ct[0,:] = -u_ct[2,:]
"""Setting top boundary ghost cell equal(*negetive) to the layer just below the
top boundary wall to null the boundary layer error"""
u_ct[-1,:] = -u_ct[-3,:]
"""Setting bottom boundary ghost cell equal(*negetive) to the layer just above the
bottom boundary wall to null the boundary layer error"""

    #"""To check if the ghost cells are working"""
    #print ("u_ct", u_ct)
    
"""For the Current time + 1: ghost cells set-up"""
u_nt[0,:] = -u_nt[2,:]
"""Setting top boundary ghost cell equal(*negetive) to the layer just below the
top boundary wall to null the boundary layer error"""
u_nt[-1,:] = -u_nt[-3,:]
"""Setting bottom boundary ghost cell equal(*negetive) to the layer just above the
bottom boundary wall to null the boundary layer error"""
    
#************************************#

#"""visualizing mesh"""

"""
 bbbbbbbbbbbbbbbbbbbbbbbbb boundary cells
 bbbbbbbbbbbbbbbbbbbbbbbbb boundary cells
 sssssssssssssssssssssssss solution points
 sssssssssssssssssssssssss solution points
 sssssssssssssssssssssssss solution points
 sssssssssssssssssssssssss solution points
 sssssssssssssssssssssssss solution points
 sssssssssssssssssssssssss solution points
 sssssssssssssssssssssssss solution points
 sssssssssssssssssssssssss solution points
 bbbbbbbbbbbbbbbbbbbbbbbbb boundary cells
 bbbbbbbbbbbbbbbbbbbbbbbbb boundary cells
"""


#************************************#
#setting up equation

"""FTCS method is being used
i = 0
j = 0 
u_ct[i,j] = (u_ct[i-1,j] + u_ct[i+1,j] + u_ct[i,j-1] + u_ct[i,j+1])/4"""

#************************************#

#setting up initial condition

for i in range(1, y_length):
    u_ct[2:-2,0] = abs(math.sin((3.54*(y_length+1)/i) + 54))




#"""Checking all the boundary conditions"""
#print(u_ct)

"""
u_ct[1:2,0:]=99 #top wall boundary
u_ct[2:3,0:]=88 #below top wall boundary
u_ct[0,:]= 101 #top ghosts
u_ct[1:2,0:]=(u_ct[2:3,0:]+u_ct[0,:])/2
print(u_ct)

u_ct[-2:-1,:]= 99 #bottom wall boundary
u_ct[-3:-2,:] = 88 #above bottom wall boundary
u_ct[-1,:]=101 #bottom ghosts

u_ct[-2:-1,:] = (u_ct[-3:-2,:]+u_ct[-1,:])/2
print(u_ct)
"""
#print(u_ct)

#************************************#

#"""SOlving the discreitized equation"""
while it < iterations:
    i=0
    j=0
    
    """Updating velocity values through FTCS iteration"""
    for i in range (1,x_length+1):
        for j in range(1,y_length+1):
            u_ct[i,j] = (u_ct[i-1,j] + u_ct[i+1,j] + u_ct[i,j-1] + u_ct[i,j+1])/4
            #u_ct[i,j] = 108 #Checking for correct selection of iteration points
    
    
    """Updating ghost cells"""
    u_ct[0,:] = -u_ct[2,:] #top boudnary
    u_ct[-1,:] = -u_ct[-3,:] #bottom boundary


    
    #"""Updating boundary conditions"""
    """Updating boundary walls"""
    u_ct[1:2,0:]=(u_ct[2:3,0:]+u_ct[0,:])/2  #updating top boundarywall 
    u_ct[-2:-1,:] = (u_ct[-3:-2,:]+u_ct[-1,:])/2 #updating bottom boundarywall
    it+=1

    """updating for neumann boundary"""
    u_ct[1:-1,-1] = u_ct[1:-1,-2]



    
    it+=1



"""updating animation"""
k = plt.imshow(u_ct[1:-1], interpolation = 'bilinear', cmap = 'RdBu')
plt.colorbar(k)
plt.show()

#print(u_ct[1:-1])



  
