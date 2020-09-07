# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A=list(dict.fromkeys(A))
    A.sort()
    
    if len(A) == 0:
        return 1
    else:
        if max(A)>0 and len(A)!=max(A):
            if min(A)>1:
                return 1
            else:
                for i in range (0,len(A)-1,1):
                    if A[i]+1 !=A[i+1]:
                        return i+2
        elif max(A)>0 and len(A)==max(A):
            f = max(A)+1
            return f
        
        else:
            return 1
    pass