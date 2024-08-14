'''
import numpy as np

def solution(nums):
    answer = 0
    
    nums = np.array(nums)
    
    N = len(nums) / 2
    n = len(np.unique(nums))
    
    if n >= N:
        answer = N
    else:
        answer = n
    
    return answer
'''
'''
import numpy as np

def solution(nums):
    nums = np.array(nums) # 중복 제거 len(set(nums))
    u = np.unique(nums)
    
    N = len(nums) / 2 # // 쓰면 int
    n = len(u)
    
    if N < n:
        return N
    else:
        return n
'''

# # min max 쓰면 간단해짐!
# def solution(nums):
#     return min(len(nums)//2, len(set(nums)))


def solution(nums):
    return min(len(set(nums)), len(nums)/2)


    
    
    
    
    

    
    
    
    
    
    
    
    
    
    