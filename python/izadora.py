
n1 = int(input("primeiro valor: "))
n2 = int(input("segundo valor: "))
n3 = int(input("terceiro valor: "))

ordenados = sorted([n1, n2, n3])

menor = ordenados[0]
meio = ordenados[1]
maior = ordenados[2]

print("Número menor:", menor)
print("Número do meio:", meio)
print("Número maior:", maior)

media = (n1+n2+n3)/3

print(f"A média dos valores é {media}")