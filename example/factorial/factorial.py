import math

def factorial(n):
    r = 1
    for i in range(1,n+1):
        r *= i
    return r

def logfactorial(n):
    r = 0
    for i in range(1,n+1):
        r += math.log(i)
        return r


if __name__ == '__main__':
    print("factorial(10)=",factorial(10))
    print('logfactorial(10)=', math.exp(logfactorial(10)))
    print('exp(logfactorial(10))=', math.exp(logfactorial(10)))
    assert round(math.exp(logfactorial(10)))==factorial(10)