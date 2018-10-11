def fibonnachi(n,m):
#example is n=5, m=8 will give 5 8 13 21 
    i1=1
    i2=1
    s=""
    i=1
    while  (i<=m) :
        if  i>=n : 
            s = s+" "+str(i1)
        t = i2
        i2=i2+i1
        i1=t
        i=i+1
    return s

print("Please enter n and m elements of Fibonnachi where m > n!") 
n = int(input("n:"))
m = int(input("m:"))
print("Range of fibonnchi numbers from",n,"to",m,"is",fibonnachi(n,m)) 
