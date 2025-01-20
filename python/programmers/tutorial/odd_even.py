def solution(n):
    answer = 0

    if(n % 2 == 0):
        # 짝수인 모든 자연수 제곱의 합
        for i in range (2, n, 2):
            answer += i ** 2
    else:
        for i in range (1, n, 2):
            answer += i
    return answer