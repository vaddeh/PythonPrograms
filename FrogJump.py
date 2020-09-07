# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    
    a = divmod((Y - X) ,D)
    if a[1] != 0:
        return a[0]+1
    else:
        return a[0]
    pass