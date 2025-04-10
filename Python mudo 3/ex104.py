def leaiint(n):
    while True:
        try:
            n = int(input(n))
            return n
        except:
            print("Valor ruim")

n = leaiint("Digite um núemero: ")
print(f"O numero digitado foi {n}")