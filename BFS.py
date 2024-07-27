class Queue:
    def __init__(self):
        self.queue=[]

def addq(self,v):
    self.queue.append(v)

def delq(self):
    v=None
    if not self.isempty:
        v=self.queue.pop(0)
    return v

def isempty(self):
    return(self.queue==[])

def __str__(self):
    return(str(self.queue))

def neighbours(AMat,i):
    nbrs=[]
    (rows,columns)=AMat.shape
    for j in range(columns):
        if AMat[i][j]==1:
            nbrs.append(j)
    return(nbrs)

def BFS(AMat,v):
    (rows,col)=AMat.shape
    visited={}
    for i in range(rows):
        visited[i]=False
    q=Queue()
    visited[v]=True
    q.addq(v)
    while(not q.isempty()):
        j=q.delq() 
        for k in neighbours(AMat,j):
            if(not visited[k]):
                visited[k]=True
                q.addq(k)
    return(visited)







