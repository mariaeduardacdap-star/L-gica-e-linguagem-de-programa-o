idade = int(input("Digite sua idade em troca de um belo conselho: "))

if idade >= 100:
    print("A vantagem de você ser muito velho é que seus segredos estão sempre seguros com seus amigos... Se eles ainda estiverem vivos.")

elif idade >= 80:
    print("Você não esqueceu, apenas guardou em um lugar profundo onde só o coração alcança.")

elif idade >= 64:
    print("Aproveite que sua paciência diminuiu, assim sobra mais tempo para o que importa: nada.")

elif idade >= 40:
    print("Meio termo né, não tem muito o que falar.")

elif idade >= 25:
    print("Nada é permanente, exceto a mudança, e essa é umas das coisas boas de ser adulto.")

elif idade >= 18:
    print("No final, somos definidos pelas escolhas que fazemos, jovem.")

elif idade >= 12:
    print("Você é apenas um adolescente em desenvolvimento, que, em meio a esse vasto universo, ainda busca algum resquicio de alegria ,esperando que ,mesmo que por um milésimo de segundo que seja, você se sinta vivo.")

elif idade >= 3:
    print("Você ainda tem uma grande jornada pela frente, pequeno gafanhoto. Você é apenas uma criança.")

elif idade >= 0:
    print("Você é só um bebê")

else:
    idade == -(idade)
    print("Raça absoluta")
