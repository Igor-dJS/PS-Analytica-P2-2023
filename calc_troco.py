# Dicionario com as notas e moedas e suas quantidades
dinheiro = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0, 0.5:0, 0.25:0, 0.10:0, 0.05:0, 0.01:0}

valor = input()
aux = valor.split(".")

# Verificando se está no padrão correto 
if len(aux) != 2 or len(aux[1]) != 2:
    print("Erro. Input inválido!")
else:
    valor = float(valor)

    # Percorrer dicionario e subtrair o valor da nota ou moeda atual do valor restante iterativamente até percorrer todas as notas
    for nota, qtd in dinheiro.items():

        var = True
        while var:
            # Caso ainda haja valor restante e seja possível subtrair sem negativar o valor restante, então adiciona 1 em quantidade
            # da nota ou moeda e subtrai seu valor 
            if (valor - nota) > 0:
                valor -= nota
                dinheiro[nota] += 1
            # Caso não seja possível, tenta com a próxima nota ou moeda menor
            else:
                var = False


# Exibe no formato pedido as notas e moedas
print("NOTAS:")
for nota, qtd in dinheiro.items():
    if nota >=2:
        print(f"{qtd} nota(s) de R$ {nota:.2f}")
    elif nota == 1:
        print("\nMOEDAS:")
        print(f"{qtd} moeda(s) de R$ {nota:.2f}")
    else:
        print(f"{qtd} moeda(s) de R$ {nota:.2f}")
