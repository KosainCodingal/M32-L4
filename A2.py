def revStr(s):
    l = len(s)
    if l == 0: return ""
    if l == 1: return s

    char = s[0]
    return revStr(s[1:]) + char
        
print(revStr("Hello World!"))
print(revStr("racecar"))