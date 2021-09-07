
#Ход короля
def g():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())

    if abs(x2-x1)<=1 and abs(y2-y1)<=1:
        print('YES')
    else:
        print('NO')

# Цвет клеток
def color():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())

    if abs(x2-x1)%2==0 and abs(y2-y1)%2==1:
        print('NO')
    elif abs(x2-x1)%2==1 and abs(y2-y1)%2==0:
        print('NO')
    elif abs(x2-x1)%2==1 and abs(y2-y1)%2==1:
        print('YES')
    elif abs(x2-x1)%2==0 and abs(y2-y1)%2==0:
        print('YES')

#Шоколадка
def Chocolate():
    n = int(input())
    m = int(input())
    k = int(input())

    if n == k or m ==k:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    Chocolate()