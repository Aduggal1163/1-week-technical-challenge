def primeChecker(n):
    if(n<2):
        return "Neither prime nor composite"
    for i in range(2,(int)(n/2)+1):
        if(n%i==0):
            return "Composite"
    return "Prime"
    
n=10
print(primeChecker(n))