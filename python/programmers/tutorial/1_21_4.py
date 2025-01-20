def solution(code):
    ret = ''; mode = 0
    
    for idx in range(0, len(code)):
        if( mode == 0 ):
            if(code[idx] != "1" and idx % 2 == 0):
                ret += code[idx]
            if(code[idx] == "1"):
                mode = 1
        else:
            if(code[idx] != "1" and idx % 2 == 1): 
                ret += code[idx]
            if(code[idx] == "1"): 
                mode = 0
            
    if(ret == ''): return "EMPTY"
    return ret

# len(code) , len(code) - 1 차이 확실하게 할 것