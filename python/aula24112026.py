anterior = int(input("Digite um número (0 para sair): "))
quantidade = 1

if anterior == 0:
    print("A sequência não é crescente. Programa encerrado!")
else:
    soma = anterior
    numero = int(input("Digite o próximo número: "))

    while numero != 0 and numero > anterior:
        soma += numero
        anterior = numero
        quantidade += 1
        numero = int(input("Digite o próximo número: "))

    print(f"A sequência não é crescente.\nA soma dos números informados foi {soma}.\nA quantidade de números foi {quantidade}.\nPrograma encerrado!")
