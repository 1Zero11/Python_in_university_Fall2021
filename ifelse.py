import itertools

#Ход короля
def g():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())

    if abs(x2-x1)>=1 and abs(y2-y1)>=1:
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

    if (n*m-k)%m == 0 or (m*n-k)%n == 0:
        print('YES')
    else:
        print('NO')

#Узник замка
def Castle_prisoner():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    if (A<=E and B<=D) or (A<=E and C<=D) or (B<=E and A<=D) or (B<=E and C<=D) or (C<=E and A<=D) or (C<=E and B<=D):
        print('YES')
    else:
        print('NO')

# Коробки
def Cardboards():
    A1 = int(input())
    B1 = int(input())
    C1 = int(input())
    A2 = int(input())
    B2 = int(input())
    C2 = int(input())

    dimensions1 = [A1, B1, C1]
    dimensions2 = [A2, B2, C2]

    possible = list(itertools.permutations([A1, B1, C1]))
    # print(possible)

    for dimensions in possible:
        if(dimensions[0]<=A2 and dimensions[1]<=B2 and dimensions[2]<=C2 or
                dimensions[0]>=A2 and dimensions[1]>=A2 and dimensions[2]>=A2):
            print('YES')
            return
    print('NO')

#Котлеты
def Cotlets():
    k = int(input())
    m = int(input())
    n = int(input())

    print((n//k + 1 - (0**(n%m)))*2*m)

if __name__ == "__main__":
    Cotlets()