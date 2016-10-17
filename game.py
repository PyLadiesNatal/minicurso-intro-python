name = input("Digite o nome: ")
size = input("Digite o tamanho: ")
while not size.isnumeric():
    if size.isnumeric():
        size = float(size)
    else:
        print('Isso nao ta certo...')
        size = 1

life = input("Digite o xp: ")
if life.isnumeric():
    life = int(life)
else:
    print('Isso nao ta certo...')
    life = 10

is_alive = True

print()
print(">> name " + name)
print(">> size " + str(size))
print(">> life " + str(life))
print(">> is alive? " + str(is_alive))