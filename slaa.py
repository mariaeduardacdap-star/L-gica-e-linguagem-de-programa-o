idade = int(input("Digite sua idade: "))

if idade >= 100:
    print("Defunto")

elif idade >= 80:
    print("Ancião")

elif idade >= 64:
    print("Idoso")

elif idade >= 40:
    print("Meia-idade")

elif idade >= 25:
    print("Adulto")

elif idade >= 18:
    print("Jovem")

elif idade >= 12:
    print("Adolescente")

elif idade >= 3:
    print("Criança")

elif idade >= 0:
    print("Bebê")

else:
    print("Idade inválida")