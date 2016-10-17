### let the games begin

Ok, vamos começar... e a sua primeira missão será easy: precisamos descrever quais caracteristicas um personagem simples terá. Por exemplo, nosso personagem com certeza tera um nome... talvez uma taxa de vida? um tamanho? seria legal saber se ele esta vivo...

```python
name = "..."
size = 1
life = 10
is_alive = True
```
    
Acho que para uma primeira descriçao, estamos indo bem. Agora vamos ao Python. 

Cada uma dessas caracteristicas que escolhemos seria o que chamamos de **variável**. Variável é uma entidade que possui um conjunto de atributos como nome, tipo e valor. Por exemplo se imaginarmos a memória de um computador como sendo uma estate de um depósito, em que cada compartimento representa um espaço de memória, podemos também imaginar uma váriável como sendo uma caixa que pode ser armazenada nessa estante.

Nessa analogia, um pouco surpeficial, dizemos que o nome da váriável é um rótulo que está associado a ela e quando formos procurar-la temos que buscar por esse rótuno. O tipo é basicamente a especificação de quais informações podem ser guardadas na caixa, ou em outras palavras, o tipo e tamanho do material que pode ser armazenado nela. Já o valor é o conteúdo armazenado dentro da caixa. Então, se dermos o nome ```idade``` a uma váriável e quisermos atribuir um valor a ela devemos fazer ```idade = 19```. Dessa forma estamos dizendo que a variável ```idade``` está recebendo o valor ```19``` que por sua vez é do tipo inteiro (```int```).

Na linguagem Python, não há a necessidade de declarar o tipo da variável; para criar uma, basta atribuir um valor a ela. Como em ```idade```. Nesse caso, o tipo da variável pode variar durante a execução do programa.

No nosso exemplo, temos ```name``` como ```str```, ```size``` como ```int``` e ```is_alive``` como ```bool```.

Nao sei se você percebeu, mas nesse exemplo os valores ja sao conhecidos... e se quisermos deixar para o usuario definir qual valor cada variavel tera? Uma função muito importante utilizada para solicidar dados do usuário é a função ```input```, vejo o que fizemos para receber o nome do nosso personagem:

```python
name = input("Digite o nome: ") 
```

Agora é importante prestar atenção para o tipo de entrada que você deseja. O ```input``` sempre vai retornar valores do tipo string. Então mesmo que seu usuário digite números, o resultado vai ser sempre string. Para corrigir isso, podemos usar a função ```int``` para converter os valores para inteiro, e a função ```float``` para converter para um número decimal.

```python
name = input("Digite o nome: ") 
size = float(input("Digite o tamanho: "))
life = int(input("Digite o xp: "))
is_alive = True
```

**IMPORATANTE**: vamos falar sobre versoes... no Python 2, temos uma outra funçao para entrada de dados, a ```raw_input```, que pega exatemante o que o usuario digitou e salva isso como uma string e o ```input```, que tenta rodar a entrada como uma expressao Python (a ideia é que ele faz o raw_input() e entao executa um eval()).
No python 3.x, ```raw_input``` foi renomeado para ```input```.

**IMPORATANTE**: *what the hell is eval???* De forma simples, a funçao ```eval``` vai interpretar a string como codigo... talvez o exemplo ajude melhor:

```python
>>> x = 1
>>> eval('x+1')
2
```