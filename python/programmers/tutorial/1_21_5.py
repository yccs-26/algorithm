def solution(a, b, c):
    answer = ( a  + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    if(a == b and b == c): return answer
    elif(a != b and b != c and c != a): return (a+b+c)
    else: return answer // (a ** 3 + b ** 3 + c ** 3)
    
    # set()도 생각해볼 것