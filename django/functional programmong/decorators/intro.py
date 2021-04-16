#in all cases smaller no should be substarcted from larger

def decorator_fun(fun):    # sub(10,20) #parameter should be a ftn
    def wrapper(n1,n2): #wrapper will be called on retuen wrapper
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fun(n1,n2)
    return wrapper

@decorator_fun
def sub(num1,num2):
    return num1-num2


res=sub(10,20)
print(res)