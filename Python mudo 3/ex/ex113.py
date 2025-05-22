def leaiint(n):
    while True:
        try:
            n = int(input(n))
            return n
        except:
            print("Valor ruim")

def leiafloat(n):
    while True:
        try:
            n = float(input(n))
            return n
        except:
            print("Valor ruim")

n = leaiint("Digite um núemero: ")
f = leaiint("Digite um núemero: ")
print(f"O numero inteiro digitado foi {n} e o outro foi {f}")