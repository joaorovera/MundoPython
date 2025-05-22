try:
    a = int(input('numero: '))
    b = int(input('numero: '))
    r = a/b
except Exception as e:
    print(f'nao deu bom, o problema encontrado foi {e.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('__--Volte sempre--__')