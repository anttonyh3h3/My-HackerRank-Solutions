    N = int(input())
    
    array = []
    while N != 0:
        A = input().split()

        if len(A) == 3:
            B = int(A[1])
            C = int(A[2])
        elif len(A) == 2:
            B = int(A[1])

        if A[0] == "insert":
            array.insert(B, C)
        elif A[0] == "print":
            print(array)
        elif A[0] == "remove":
            array.remove(B)
        elif A[0] == "append":
            array.append(B)
        elif A[0] == "sort":
            array.sort()
        elif A[0] == "pop":
            array.pop()
        elif A[0] == "reverse":
            array.reverse()
        N -= 1
