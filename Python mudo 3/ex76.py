lista = (
    "carne", 27.50,
    "frango", 15.00,
    "peixe", 22.00,
    "arroz", 5.50,
    "feijão", 4.00,
    "macarrão", 3.50,
    "batata", 2.80,
    "tomate", 6.00,
    "alface", 2.00,
    "cenoura", 3.00
)

print("-" * 20)
print("LISTAGEM DE PREÇOS")
print("-" * 20) 
for i in range(0,len(lista)):
    if i%2==0:
        print(f"{lista[i]:.<30} R${lista[i+1]}")