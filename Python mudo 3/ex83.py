def verifica_expressao(expressao):
    pilha = []
    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                return False
    return len(pilha) == 0

expressao = input("Digite uma expressão: ")
if verifica_expressao(expressao):
    print("A expressão está correta!")
else:
    print("A expressão está incorreta!")