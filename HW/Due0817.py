T = int(input())
for n in range(T):
    a , b = input().split()
    try:
        answer = int(a) // int(b)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as err:
        print("Error Code:", err)
    else:
        print(answer)