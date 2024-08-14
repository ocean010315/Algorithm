'''
def solution(participant, completion):
    answer = ''
    
    # hash(p)가 key, p가 value인 hash_map 만들기
    # sum에는 hash값들 더해주기(서로 다른 p라면 고유한 값을 가지는 hash의 성질 이용)
    hash_map = {}
    sum = 0
    for p in participant:
        hash_map[hash(p)] = p
        sum += hash(p)
        
    for c in completion:
        sum -= hash(c)
    
    answer = hash_map[sum]
    
    return answer
'''
# def solution(participant, completion):
#     dict = {}
#     sum = 0
    
#     for p in participant:
#         dict[hash(p)] = p
#         sum += hash(p)
        
#     for c in completion:
#         sum -= hash(c)
    
#     return dict[sum]

def solution(participant, completion):
    dict = {}
    sum = 0
    for p in participant:
        sum += hash(p)
        dict[hash(p)] = p
    
    for c in completion:
        sum -= hash(c)
    
    return dict[sum]









    
    

    
    
    