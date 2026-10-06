valor = float(input("Qual o valor do produto? "))
if valor >=200:
    print("Frete grátis!")
    print("O valor final é", valor)
elif valor>=100:
    print("Frete = R$10,00.")
    frete = 10
    valordoproduto = frete+valor
    print("Frete R$10,00. O valor final é ", valordoproduto)
else:
    frete=20
    valordoproduto = frete+valor
    print("Frete R$10,00. O valor final é ", valordoproduto)
