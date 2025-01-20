def solution(a, d, included):
    sum = 0
    for i in range(0, len(included)):
        if( included[i] == True ):
            sum += a + d * i
    return sum