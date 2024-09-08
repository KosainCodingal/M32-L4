def rev(n):
    if n > 0: 
        p = n%10
        if n//10 > 0:
            c = rev((int)(n//10))
            return p * (10 ** len(str(c))) + c
        return n
        
print(rev(1234))
print(rev(10305070))