# Точная степень двойки
def degreeoftwo():

    n = int(input())

    if n == 1:
        print('YES')
        return

    while n%2==0:
        n= n//2
        if n==1:
            print('YES')
            return
    print('NO')

# Пробежка
def Probeg():
    x = int(input())
    y = int(input())

    days = 0

    while x <= y:
        days+=1
        x*=1.1
    print(days)

def max2():
    arr = input().split()

    max1 = 0
    max2 = 0

    for i in range(len(arr)):
        if int(arr[i]) > max1:
            max2 = max1
            max1 = int(arr[i])
        elif int(arr[i]) > max2:
            max2 = int(arr[i])

    print(max2)

def nubmerOfMax():
    arr = input().split()

    max1 = 0

    for i in range(len(arr)):
        if int(arr[i]) > max1:
            max1 = int(arr[i])

    count = 0
    for i in range(len(arr)):
        if int(arr[i]) == max1:
            count+=1

    print(count)

def reverse(str = ''):
    if str=='':
        str = input()
    return (str[::-1])

def palindrom():
    k = int(input())

    count = 0

    for i in range(1,k):
        if str(i) == reverse(str(i)):
            count+=1

    print(count)

def monoton():
    arr = input().split()

    maxmonot = 0

    previous = int(arr[0])

    count = 1

    up = True

    for i in range(1, len(arr)):
        # print(previous, int(arr[i]))

        if previous < int(arr[i]):
            if up:
                count+=1
            else:
                if maxmonot<count:
                    maxmonot = count
                count = 2
                up = True

        elif previous > int(arr[i]):
            if not up:
                count+=1
            else:
                if maxmonot<count:
                    maxmonot = count
                count = 2
                up = False
        previous = int(arr[i])

    print(max(count, maxmonot))

# Наименьшее расстояние между локальными максимумами
def maxlen():
    arr = input().split()

    maxindexes = []
    for i in range(1, len(arr)-1):
        if arr[i-1]<arr[i] and arr[i+1]<arr[i]:
            maxindexes.append(i)
    # print(maxindexes)
    if(len(maxindexes)<2):
        print(0)
    else:
        min = len(maxindexes)
        previous = maxindexes[0]
        for i in range(1, len(maxindexes)):
            if maxindexes[i] - maxindexes[i-1] < min:
                min = maxindexes[i] - maxindexes[i-1]
        print(min)



if __name__ == "__main__":
    maxlen()