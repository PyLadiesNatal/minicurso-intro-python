## Again, again, again...

Você já deve ter se deparado com códigos que precisavam ser executados várias vezes em função de alguma condição. Um exemplo simples seria a entrada de dados do nosso jogo... enquanto o jogador não inserir o valor correto, vamos continuar pedindo que ele digite.

Uma das estruturas que o Python disponibiliza é o ``while```. Ele vai repetir um bloco de código enquanto uma condição for verdadeira.

```python
x = 0
while x <= 10:
    print(x)
    x = x + 1
```

No nosso exemplo, enquanto o valor da variável ```x``` for menor ou igual a 10, vamos imprimir o seu valor, somar +1, e repetir o laço.

Uma possibilidade para nosso jogo é pedir o valor da ```life``` até que o usuário digite o valor correto.

```python
while True:
    life = input("Digite a life: ")
    if life.isnumeric() and 0 < life <= 20:
        life = float(life)
        break
    else:
        print('Isso nao ta certo...')
```

Vamos aproveitar esse exemplo para falar sobre a instruçāo ```break``` , que interrompe a execução do ```while```, caso o valor de ```life``` seja numérico e esteja entre 1 e 20.

Uma outra estrutura importante é o ```for```, que nós usamos em nosso exemplo com uma informaçao adicional: as skills. Criamos três skill básicas:

```python
skills = ['força', 'destreza', 'inteligência']
```

Caso você nao saiba que estrutura é esta, falaremos sobre ela melhor mais para frente, no momento basta saber que esta é uma lista em Python. 

Criamos também uma lista para os valores de cada skill, e utilizamos o ```for``` para "caminhar" pela lista:

```python
skills = ['força', 'destreza', 'inteligência']
skills_values = []
for skill in skills:
    value = float(input("Digite um valor para a skill {}: ".format(skill)))
    skills_values.append(value)
```

Basicamente este ```for``` vai atribuir a ```skill``` cada falar armazanado em ```skills```, seguindo a sequência em que eles aparecem. Ou seja:

1) skill = 'força'
2) skill = 'destreza'
3) skill = 'inteligência'

Também usamos o ```for``` quando imprimimos a lista de skill com seus valores:

```python 
for skill, value in zip(skills, skills_values):
    print(">> skill {} - {}".format(skill, value))
```

**CURIOSIDADE**: no nosso exemplo usamos a funçao ```zip()```, a ideia dela é fazer um iterador que agrega elementos de cada uma das listas. Mas para frente estudaremos uma estrutura de dados chamada tupla, e podemos voltar a esta função e entendê-la melhor, mas resumidamente teremos:

    zip('ABCD', 'xyzw') --> Ax By Cz Dw