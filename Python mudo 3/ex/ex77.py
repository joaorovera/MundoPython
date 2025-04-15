palavras = ('python', 'programacao', 'desenvolvimento', 'codigo', 'computador', 'algoritmo', 'software', 'hardware')
for i in palavras:
    print(f"\nEm {i} temos as vogais:", end=" ")
    for letra in i:
        if letra.lower() in "aeiou":
            print(letra, end=" ")