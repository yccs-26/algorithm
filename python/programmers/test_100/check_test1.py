def solution(a, b, n):
    answer = 0
    while(n >= a):
        answer = answer + (n // a) * b
        n = (n % a) + (n // a) * b
    return answer