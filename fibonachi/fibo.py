import typing

buffer = [ 0, 1, 1, 2, 3, 5 ]

def fibo(n: int):
    if len(buffer) >= n + 1:
        return buffer[n]

    buff_length = len(buffer)
    f1: int = buffer[buff_length - 2]
    f2: int = buffer[buff_length - 1]

    for i in range(buff_length-1, n):
        tmp = f1
        f1 = f2
        f2 = tmp + f2
        buffer.append(f2)
        print(f"buffer: {buffer}")

    return f2


# fibo(0) = 0
# fibo(1) = 1

# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
# 
#     return fibo(n-1) + fibo(n-2)
