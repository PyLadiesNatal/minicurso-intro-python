# Filas

Nossa vida é rodeada de filas. Seja no banco, mercado ou cinema, as chances são altas de acabar caindo em uma fila.

Mas afinal, como funciona uma fila?

## O primeiro que entra é o primeiro que sai

A característica principal de uma fila é que o primeiro que entra é o primeiro que sai, também chamado de *First In First Out* ou *FIFO*.

De acordo com a Wikipedia:

*"As listas são amplamente utilizadas em programação para implementar filas de espera. Em uma fila de tipo FIFO os elementos vão sendo colocados na fila e retirados (ou processados) por ordem de chegada. A ideia fundamental da fila é que só podemos inserir um novo elemento no final da fila e só podemos retirar o elemento do início."*

## Chega de teoria, eu quero prática.

Primeiro vamos criar uma classe que tenha as características de uma fila:

```python
class Fila:
    def __init__(self): # Construtor da classe
        self.fila = []
    def __repr__(self): # Retorna uma representação visual do objeto
        return self.fila.__repr__()
    def tamanho(self):
        return len(self.fila) # Retorna o tamanho da fila
    def adicionar(self, x): # Adiciona itens no fim da fila
        self.fila.append(x)
    def remover(self): # Remove itens do início da fila caso ela não esteja vazia
        if self.tamanho() != 0:
            del self.fila[0]
```

Agora instanciamos a classe:
```python
>>> f = Fila()
```

Certo, vamos ver quantas pessoas estão na fila:
```python
>>> f.tamanho()
0
```

Até agora ninguém! Mas assim não tem graça! Que tal adicionarmos algumas pessoas?
```python
>>> f.adicionar('Huguinho')
>>> f.adicionar('Zezinho')
>>> f.adicionar('Luizinho')
>>> f.tamanho()
3
>>> print(f)
['Huguinho', 'Zezinho', 'Luizinho']
```

Perfeito! Agora, que tal fazermos a fila andar?
```python
>>> print(f)
['Huguinho', 'Zezinho', 'Luizinho']
>>> f.remover()
>>> print(f)
['Zezinho', 'Luizinho']
```
Repare que o Huguinho foi o primeiro a entrar na fila e o primeiro a sair, tal qual uma fila de verdade.

Pra finalizar, vamos brincar mais um pouco:
```python
>>> print(f)
['Zezinho', 'Luizinho']
>>> f.remover()
>>> print(f)
['Luizinho']
>>> f.adicionar('Donald')
>>> f.adicionar('Pateta')
>>> print(f)
['Luizinho', 'Donald', 'Pateta']
>>> f.remover()
>>> print(f)
['Donald', 'Pateta']
>>> f.remover()
>>> print(f)
['Pateta']
>>> f.remover()
>>> print(f)
[]

```
