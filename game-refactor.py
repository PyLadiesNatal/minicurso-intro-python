# coding=utf-8
personagem = {}
skills = {'força', 'destreza', 'inteligência'}
ataques = [('tapa na cara', 1), ('voadora', 2)]


def input_data(n_players):
    global skills, ataques
    player = 0
    while player != n_players:
        player += 1
        name = input("Digite o nome: ")
        personagem['name'] = name

        while True:
            size = input("Digite o tamanho: ")
            if size.isnumeric():
                personagem['size'] = float(size)
                if 0 < personagem['size'] <= 3:
                    personagem['height'] = "short"
                elif 3 < personagem['size'] <= 7:
                    personagem['height'] = "medium"
                else:
                    personagem['height'] = "tall"
                break
            else:
                print('O valor digitado precisa ser numérico e estar no intervalo de 1 a 10.')

        while True:
            life = input("Digite a life: ")
            if life.isnumeric() and 0 < float(life) <= 20:
                personagem['life'] = float(life)
                break
            else:
                print('O valor digitado precisa ser numérico e estar no intervalo de 1 a 20.')

        personagem['is_alive'] = True

        skills_values = {}
        for skill in skills:
            value = float(input("Digite um valor para a skill {}: ".format(skill)))
            skills_values[skill] = value

        personagem['skills'] = skills_values


def print_data(personagem):
    print()
    print(">> name " + personagem['name'])
    print(">> size " + str(personagem['size']))
    print(">> life " + str(personagem['life']))
    print(">> is alive? " + str(personagem['is_alive']))
    for k, v in personagem['skills'].items():
        print(">> skill {} - {}".format(k, v))


def run():
    while personagem:
        rodada = list(personagem.keys())


def play():
    n_players = input("Digite o numero de jogadores: ")
    input_data(n_players)

if __name__ == "__main__":
    play()
