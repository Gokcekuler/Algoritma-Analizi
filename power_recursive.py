import time
recursive_sayac=0
loop_sayac=0
def power_recursive(m,n):
    global recursive_sayac
    recursive_sayac=recursive_sayac +1
    if(n==0):
        return 1
    elif (n==1):
        return m

    elif(n%2==0):
        return power_recursive(m*m, n//2)
    elif(n%2 !=0):
        return power_recursive(m*m, n//2)*m

def power_loop(m,n):
    global loop_sayac
    s=1
    for i in range(n):
        s=s*m
        loop_sayac=loop_sayac+1
    return s
recursivestart=time.time()
print(power_recursive(4,50))
recursivefinish=time.time()
print(recursivefinish-recursivestart)
loops=time.time()
print(power_loop(4,50))
loopf=time.time()
print(loopf-loops)






