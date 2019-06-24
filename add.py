
def myinput():
    a=int(input("Enter a"))
    b=int(input("Enter b"))
    return a,b
def add(a,b):
    return a+b
def myprint(a,b,mysum):
    print("%d + %d = %d"%(a,b,mysum))
def main():
    a,b=myinput()
    s=add(a,b)
    myprint(a,b,s)
    
