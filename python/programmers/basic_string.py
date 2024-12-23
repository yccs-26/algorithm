def solution(a, b):
    ab = int( str(a) + str(b) )
    ba = int( str(b) + str(a) )
    if( ab > ba ):
        return ab
    else:
        return ba
    
# 삼항 연산자는 조건문 안에서 사용해야 하는데 여기서는 조건문 밖에서 사용하고 있기 때문이다.

# python에서 string 안에 변수를 사용할 때 {}를 사용하여 변수를 사용한다.
# 이때 숫자를 사용할 때는 문장 앞에 f를 붙여준다.
# n = 5
# print(f"n = {n}")