# coding=utf-8
name = input("Digite o nome: ")
height = ""
size = 0
life = 0

while True:
    size = input("Digite o tamanho: ")
    if size.isnumeric():
        size = float(size)
        if 0 < size <= 3:
            height = "short"
        elif 3 < size <= 7:
            height = "medium"
        else:
            height = "tall"
        break
    else:
        print('O valor digitador precisa ser numérico e estar no intervalo de 1 a 10.')

while True:
    life = input("Digite a life: ")
    if life.isnumeric() and 0 < float(life) <= 20:
        life = float(life)
        break
    else:
        print('Isso nao ta certo...')


is_alive = True

skills = ['força', 'destreza', 'inteligência']
skills_values = []
for skill in skills:
    value = float(input("Digite um valor para a skill {}: ".format(skill)))
    skills_values.append(value)

print()
print(">> name " + name)
print(">> size " + str(size))
print(">> life " + str(life))
print(">> is alive? " + str(is_alive))
for skill, value in zip(skills, skills_values):
    print(">> skill {} - {}".format(skill, value))