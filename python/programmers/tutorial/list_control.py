def solution(arr, query):
    answer = ''
    for i in query:
        if( i % 2 == 0):
            answer = arr[1:]
        else:
            answer = arr[2:len(arr)]
    return answer

print(solution([0, 1, 2, 3, 4, 5], [4, 1, 2]))