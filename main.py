# F
def f():
    val = int(input("Enter a value: "))
    print((val % 100)//10)

# M
def f():
    name = input()
    print("Hello, ", name, "!", sep="")

#U
def u():
    h = int(input())
    a = int(input())
    b = int(input())

    height = (h-a)//(a-b) + (h-a)%(a-b)//(h-a)%(a-b) + 1
    print(height)


#H
def h():
    bt = int(input())
    print(1 - 1*bt)


#W
def w():
    a = int(input())
    b = int(input())
    print((a%b//a%b)*b + (b%a//b%a)*a + (1-(a//b + b//a)%2)*a)


#X
def x():
    a = int(input())
    b = int(input())

    print("Yes"*(0**(a%b)) + "No"*(1-0**(a%b)))

#Q
def q():
    inp = int(input())
    print(str(inp//3600) + ":" + str(inp%3600//600) + str(inp%3600%600//60) + ":" + str(inp%3600%600%60//10) + str(inp%3600%600%60%10))

#R
def r():
    a = int(input())
    b = int(input())
    amount = int(input())
    print(a*amount+b*amount//100, b*amount%100)

if __name__ == "__main__":
    r()