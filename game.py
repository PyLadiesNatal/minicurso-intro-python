name = input("Digite o nome: ")
while True:
    size = input("Digite o tamanho: ")
    if size.isnumeric():
        size = float(size)
        break
    else:
        print('Isso nao ta certo...')

life = input("Digite o xp: ")
while True:
    life = input("Digite o tamanho: ")
    if life.isnumeric():
        life = float(size)
        break
    else:
        print('Isso nao ta certo...')

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