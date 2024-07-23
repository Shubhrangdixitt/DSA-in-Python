#code to form a matrix with the edges given 
edges=[(0,1),(0,4),(1,2),(2,0),(3,4),(3,6),(4,0),(4,3),(4,7),(5,3),(5,7),(6,5),(7,4),(7,8),(8,5),(8,9),(9,8)] #random example of edges in a graph
import numpy as np
A=np.zeros(shape=(10,10)) #used to form matrix with all 0 values
for (i,j) in edges:
    A[i][j]=1 #changes the value in matrix if edge of particular row and column number is present 
print(A)

#code to find the neighbours in the matrix
def neighbours(AMat,i):
    nbrs=[]
    (rows,columns)=AMat.shape
    for j in range(columns):
        if AMat[i][j]==1:
            nbrs.append(j)
    return(nbrs)
print(neighbours(A,7))

#code to find adjacency list which is the neighbours for every single vertex
def adjlist(AMat):
    rows=len(AMat)
    adjlist=[]
    for i in range(rows):
        adjlist.append(neighbours(AMat,i))
    return(adjlist)
print(adjlist(A))


