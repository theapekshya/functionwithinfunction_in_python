#function within function

def display():
    a='apekshya'
    print(a)

def add():
    display()   #function within function
    b=10
    c=5
    d=b+c
    print(d)
add()