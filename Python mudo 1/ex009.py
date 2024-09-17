n = int(input('Digite o numero que deseja ver a tabuada: '))
i = 1
print('='*20)

while i < 11:
    print(f'{n} x {i:2} = {n*i}')
    i+=1

print('='*20)