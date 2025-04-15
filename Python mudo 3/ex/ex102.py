def fatorial(num,show=False):
    if show:
        for i in range (num,0,-1):
            print(i,end=' ')
            if i > 1:
                print('x',end=' ')
    for i in range (num-1,0,-1):
            num *= i
    return(f'= {num}')

print(fatorial(5,True))