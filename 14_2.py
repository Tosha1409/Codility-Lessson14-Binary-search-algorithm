#checking is n nails enough to nail all planks
def check(Z,C,n,last):
    nails_array=[0]*(last+1)
    for m in range(0,n): nails_array[C[m]]=1
    for m in range(1,last+1): nails_array[m] += nails_array[m-1]
    for plank in Z: 
        if (nails_array[plank[0]-1] - nails_array[plank[1]]==0): return False
    return True


def solution(A, B, C):
    minp=1
    maxp=len(C)
    last_plank=max(max(B),max(C))
    Z=list(zip (A,B))
    
    result=-1
    while (minp<=maxp):
        midl=(minp+maxp)//2
        if check(Z,C,midl,last_plank): 
            maxp=midl-1
            result=midl
        else:
            minp=midl+1

    return (result)