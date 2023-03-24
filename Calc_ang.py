hor = "0"

# Recebe input enquanto não for digitado 'f'
while hor != "f":
    hor = input()
    if hor == "f": continue
    lista = hor.split(":")

    # Verificar se há horas e minutos
    if len(lista) != 2:
        print("Input inválido")
        continue

    # Verificar se tanto as horas quanto minutos possui dois digitos
    if len(lista[0]) != 2 or len(lista[1]) != 2:
        print("Input inválido")
        continue

    # Convertendo as horas e minutos para inteiro para melhor manipulação
    horas = int(lista[0])
    minutos = int(lista[1])

    # Verifica se as horas e minutos estão dentro dos limites certos
    if horas > 23 or horas < 0 or minutos > 59 or minutos < 0:
        print("Input inválido")
        continue

    # Calcula o ângulo entre os ponteiros dividindo o angulo de acordo com a quantidade de horas e minutos de um relógio
    res = abs(((horas % 12) * 360 / 12) - (minutos * 360 / 60))
    print(f"O menor ângulo é de {int(res)}º")


print("Fim...")