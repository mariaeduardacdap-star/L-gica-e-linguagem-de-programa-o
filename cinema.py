#código identifica se tem permissão para
#assistir filmes +16
idade = int(input("Digite sua idade: "))
#só aceita número inteiro
if idade >= 16:
    print("Entrada permitida!")
else:
    print("Entrada não permitida!")