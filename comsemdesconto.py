valor = float(input("Digite o valor: "))
if valor >=500:
    print("Desconto de 20%!")
    desconto=valor*0.20
    valorcomdesconto=valor-desconto
    print("O valor do produto é", valorcomdesconto)
elif valor >=200:
    print("Desconto de 10%!")
    desconto=valor*0.10
    valorcomdesconto=valor-desconto
    print("O valor do produto é", valorcomdesconto)
else:
    print("Sem desconto.")
