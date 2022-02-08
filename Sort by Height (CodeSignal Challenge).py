def solution(a):
    index = []
    order = []
    for i in range(0,len(a)):
        if a[i] == -1:
            index.append(i)  
    for num in a:
        if num != -1:
            order.append(num)
    x = sorted(order)
    for y in index:
        x.insert(y, -1)
    return(x)

