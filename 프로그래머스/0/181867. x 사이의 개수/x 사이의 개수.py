def solution(myString):
    strArr = myString.split("x")
    
    return [len(n) for n in strArr]