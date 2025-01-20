def solution(my_string):
    answer = my_string.split()
    return answer

# 파이썬에서 문자열은 불변이므로 
# split, upper, lower, join, replace, strip
# 와 같은 메소드들은 새로운 문자열을 반환한다.

# 문자열을 변경하고 싶다면 변수에 할당하여 사용해야 한다.
# 예를 들어, my_string = my_string.split() 와 같이 사용해야 한다.
