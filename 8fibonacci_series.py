# fibonacci_series
# 0 1 1 2 3 5 8 13 21 34

def fibonacci_seq(n):
    a= 0   # first number     ,a=1
    b = 1  # second number     , b=1
    if n == 1:
        print(a)
    elif n == 2:
        print(b)
    else:
        print(a,b ,end= " ")   # a b , 0 1
        for i in range(n-2):
            c = a + b   # c=1 ,2 ,3
            a = b       # a=1 , 1, 2
            b = c       # b=1 ,2 , 3 
            print(b , end= " ")      
print(fibonacci_seq(10))