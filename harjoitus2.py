#Markus Koski
print("Hello World")

def hello(n):
    if n == 1:
        print("!!!")
        return 1
    else:
        print("Hello", end=" ")
        return hello(n - 1)

hello(4)