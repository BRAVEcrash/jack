def calc(n1, x,n2):
    n1, n2 = map(int, (n1, n2))
    if x== '+':
        return n1+n2
    elif x =='-':
        return n1-n2
    elif x == '*':
        return n1*n2
    elif x=="/":
        return n1/n2
    else:
        return "error"
    
while True:
    n1, x, n2 = input("write number and operation method: stop:").split()
    temp = calc(n1,x,n2)
    if temp != 'error': print(temp)
    else: break

