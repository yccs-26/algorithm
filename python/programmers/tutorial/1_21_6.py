def solution(num_list):
    temp = 1
    for i in num_list:
        temp *= i
    return 1 if(sum(num_list)**2 > temp) else 0