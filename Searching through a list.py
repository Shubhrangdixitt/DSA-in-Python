#Naive way of searching through a list
def naivesearch(v,l: list):
    for x in l:
        if x==v:
            return True
    return False
 
#Better way of searching through a list
def binarysearch(v,l):
    if l == []:
        return False
    m=len(l)//2
    if v==l[m]:
        return True
    if(v<l[m]):
        return(binarysearch(v,l[:m]))
    if(v>l[m]):
        return(binarysearch(v,l[m+1:]))