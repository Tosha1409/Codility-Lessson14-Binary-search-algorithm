def solution(K, M, A):
    #counting prefix sums
    B=[0]
    s=0
    start=0
    finish=len(A)
    for x in range(0,len(A)):
        s += A[x]
        B.append(s)

    #main part
    mina=max(A)
    maxa=B[-1]
    while (mina<=maxa):
        midl=(mina+maxa)//2
        c=0
        pieces=0
        for e in range (1, finish+1):
            if (B[e]-c>midl):
                c=B[e-1]
                pieces +=1
        if c!=B[-1]: pieces+=1
        if pieces>K: mina= midl+1
        else: maxa=midl-1
    
    return(mina)    