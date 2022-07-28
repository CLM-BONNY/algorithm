def hanoiTop(first, second, third, count):
    if count == 1:
        print(first, third)
        return
    
    hanoiTop(first, third, second, count-1)
    print(first,third)
 
    hanoiTop(second, first, third, count-1)
 
n = int(input())

print(2 ** n - 1)
 
if n <= 20:
    hanoiTop(1, 2, 3, n)
