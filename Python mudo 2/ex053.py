f = input('Escreva uma frase ou palavra: ').replace(" ","")
t = f[::-1]
if f == t:
    print('é palindromo')
else:
    print('não')
