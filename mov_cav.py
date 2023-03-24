import string
pos = "0"

# Listas com as posições das colunas(x) e linhas(y) do tabuleiro
x = list(string.ascii_lowercase[:8])
y = list(map(str,list(range(1,9))))

# Função que nos devolve o índice de uma posição nas listas
def acha_index(valor, lista):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i

#Cria uma lista com todas posições que é possível alcançar dada uma posição no tabuleiro
def gera_pos_possiveis(pos):
    lista = []
    eixo_x = acha_index(pos[0], x)
    eixo_y = acha_index(pos[1], y)

    # Verifica se os movimentos possíveis estão dentro dos limites do tabuleiro e se sim adiciona a lista de possibilidades de movimento
    if (eixo_x - 2) >= 0:
        if (eixo_y + 1) < 8:
            lista.append(x[eixo_x - 2] + y[eixo_y + 1])

        if (eixo_y - 1) >= 0:
            lista.append(x[eixo_x - 2] + y[eixo_y - 1]) 

    if (eixo_x - 1) >= 0:
        if (eixo_y + 2) < 8:
            lista.append(x[eixo_x - 1] + y[eixo_y + 2])

        if (eixo_y - 2) >= 0:
            lista.append(x[eixo_x - 1] + y[eixo_y - 2])

    if (eixo_x + 1) < 8:
        if (eixo_y + 2) < 8:
            lista.append(x[eixo_x + 1] + y[eixo_y + 2])

        if (eixo_y - 2) >= 0:
            lista.append(x[eixo_x + 1] + y[eixo_y - 2]) 

    if (eixo_x + 2) < 8:
        if (eixo_y + 1) < 8:
            lista.append(x[eixo_x + 2] + y[eixo_y +1])

        if (eixo_y - 1) >= 0:
            lista.append(x[eixo_x + 2] + y[eixo_y - 1])

    return lista
     

# Recebe input enquanto não for digitado 'f'
while pos != "f":
    pos = input()
    if pos == "f": continue
    lista = pos.split(" ")

    # Verifica se há duas posições no input
    if len(lista) != 2:
        print("INVÁLIDO")
        continue

    # Separando posições para melhor organização    
    pos_atual = lista[0]
    pos_fut = lista[1]

    # Verifica se as posições têm dois caracteres
    if len(pos_atual) != 2 or len(pos_fut) != 2:
        print("INVÁLIDO")
        continue

    # Verificando se as posições são válidas
    if (not pos_atual[0] in x) or (not pos_atual[1] in y) or (not pos_fut[0] in x) or (not pos_fut[1] in y):
        print("INVÁLIDO")
        continue

    # Obtem as posições possíveis para qual é possível se mover
    pos_possiveis = gera_pos_possiveis(pos_atual)

    # Caso a posição para qual se quer movimentar está dentro das possibilidade de movimentação, então o movimento é válido
    if pos_fut in pos_possiveis:
        print("VÁLIDO")
    else:
        print("INVÁLIDO")

print("Fim...")
