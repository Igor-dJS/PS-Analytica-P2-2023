num = 0
# Dicionario que recebera os num e aumentara sua freqeuncia de acordo com as ocorrencias deles
dic = {}

# Recebe input enquanto não for digitado 'f'
while num != "f":
    num = input()
    if num == "f": continue

    # Ignora os inputs que não são números
    try:
        num = int(num)
    except ValueError:
        continue

    # Se o num não estiver no dicionario então contabiliza 1, caso contrário adiciona 1 a freqeuncia atual
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

# Exibe no formato pedido
for num, qtd in dic.items():
    if qtd == 1:
        print(f"O número {num} apareceu 1 vez")
    else:
        print(f"O número {num} apareceu {qtd} vezes")

print("Fim...")