# 연속 되는 원소는 하나만 남기도록 하는 배열 활용 문제
# https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    answer.append(arr[0])
    
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
    return answer