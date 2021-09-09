import itertools


# Ход короля
def g():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())

    if abs(x2 - x1) >= 1 and abs(y2 - y1) >= 1:
        print('YES')
    else:
        print('NO')


# Цвет клеток
def color():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())

    if abs(x2 - x1) % 2 == 0 and abs(y2 - y1) % 2 == 1:
        print('NO')
    elif abs(x2 - x1) % 2 == 1 and abs(y2 - y1) % 2 == 0:
        print('NO')
    elif abs(x2 - x1) % 2 == 1 and abs(y2 - y1) % 2 == 1:
        print('YES')
    elif abs(x2 - x1) % 2 == 0 and abs(y2 - y1) % 2 == 0:
        print('YES')


# Шоколадка
def Chocolate():
    n = int(input())
    m = int(input())
    k = int(input())

    if (n * m - k) % m == 0 or (m * n - k) % n == 0:
        print('YES')
    else:
        print('NO')


# Узник замка
def Castle_prisoner():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    if (A <= E and B <= D) or (A <= E and C <= D) or (B <= E and A <= D) or (B <= E and C <= D) or (
            C <= E and A <= D) or (C <= E and B <= D):
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
    #print(possible)

    for dimensions in possible:
        if (dimensions[0] <= A2 and dimensions[1] <= B2 and dimensions[2] <= C2 or
                dimensions[0] >= A2 and dimensions[1] >= B2 and dimensions[2] >= C2):
            print('YES')
            return
    print('NO')


# Котлеты
def Cotlets():
    k = int(input())
    m = int(input())
    n = int(input())

    print((n // k + 1 - (0 ** (n % m))) * 2 * m)


# Спички
def Spichki():
    l1 = int(input())
    r1 = int(input())
    l2 = int(input())
    r2 = int(input())
    l3 = int(input())
    r3 = int(input())

    conn = [(l1, r1), (l2, r2), (l3, r3)]
    if isconnectedthree(conn):
        return 0
    else:

        dif = r1 - l1
        if l2 < l3:
            newconn = [(r2, r2 + dif), (l2, r2), (l3, r3)]
            if (isconnectedthree(newconn)):
                return 1
        else:
            newconn = [(r3, r3 + dif), (l2, r2), (l3, r3)]
            if (isconnectedthree(newconn)):
                return 1

        dif = r2 - l2
        if l1 < l3:
            newconn = [(r1, r1 + dif), (l1, r1), (l3, r3)]
            if (isconnectedthree(newconn)):
                return 2
        else:
            newconn = [(r3, r3 + dif), (l1, r1), (l3, r3)]
            if (isconnectedthree(newconn)):
                return 2

        dif = r3 - l3
        if l1 < l2:
            newconn = [(r1, r1 + dif), (l1, r1), (l2, r2)]
            if (isconnectedthree(newconn)):
                return 3
        else:
            newconn = [(r2, r2 + dif), (l1, r1), (l2, r2)]
            if (isconnectedthree(newconn)):
                return 3


def isconnected(s1, s2):
    if s1[0] <= s2[0] <= s1[1] or s2[0] <= s1[0] <= s2[1]:
        return True
    else:
        return False


def isconnectedthree(conn):
    if (isconnected(conn[0], conn[1]) and isconnected(conn[1], conn[2]) or
            isconnected(conn[0], conn[1]) and isconnected(conn[0], conn[2]) or
            isconnected(conn[0], conn[2]) and isconnected(conn[1], conn[2])):
        return True
    else:
        return False


if __name__ == "__main__":
    Cardboards()
