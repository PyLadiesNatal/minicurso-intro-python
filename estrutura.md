# Vamos ver algo um pouco diferente...

Você deve lembrar que nas sessões anteriores vimos alguns tipos básicos em Python, agora nós vamos abordar alguns tipos diferentes, como listas, sets, dicionários, tuplas, etc.

* Listas

Variáveis do tipo Lista, permitem armazenar vários valores e os deixam disponíveis para serem acessados através de índices.Os valores armazenados em uma lista podem ser do mesmo tipo, de diferentes tipos ou podem ser até mesmo outras listas.

```python
a = [66.25, 333, 333, 1, 1234.5]
```
Neste exemplo temos a lista ```a```, com 5 valores: 66.25, 333, 333, 1, 1234.5. Dizemos que ela tem 5 elementos, que podem ser acessados por seus índices, por exemplo, usando a referência a[0], poderemos acessar o valor 66.25, já com a[3], acessaremos o valor 333. Para modificar uma lista, basta fazer a atribuição de um novo valor a uma posição da lista, por exemplo, a[5] = 55. Perceba que quando for tentar acessar o valor de a[5], será exibido 55.

```python
list.insert(5,55)
```

Usando como fonte a Documentação Python, podemos listar todos os métodos disponíveis em um objeto lista:

```list.append(x)```: Adiciona um item ao fim da lista.
```list.extend(L)```: Prolonga a lista, adicionando no fim todos os elementos da lista L passada como argumento.
```list.remove(x)```: Remove o primeiro item encontrado na lista cujo valor é igual a x.

```python
a.remove(333)
```

```list.pop([i])```: Remove o item na posição dada e devolve.
```list.index(x)```: Devolve índice do primeiro item cujo valor é igual a x.

```python
>>> a.index(333)
```

```list.count(x)```: Devolve o número de vezes que o valor x aparece na lista.

```python
>>> print a.count(333), a.count(66.25), a.count('x')
```

```list.sort()```: Ordena os itens na própria lista.

```python
>>> a.sort()
```

```list.reverse()```: Inverte a ordem dos elementos da lista.

```python
>>> a.reverse()
```
* Usando listas como filas
Você também pode usar uma lista como uma fila, mas para isso ela deve obedecer algumas regras com relação a inclusão e remoção de um elemento.No caso das filas, o primeiro item adicionado é o primeiro a ser recuperado (“primeiro a entrar, primeiro a sair”, FIFO, "first in first out").

```Adicionando elemento na fila:```

```python
a.append(teste)
```

```Removendo elemento da fila:```
```python
a.pop(3)
```

* Usando listas como pilhas
Sua política funciona basicamente com a adição de um item no topo e a remoção também é feita no topo (política “último a entrar, primeiro a sair”, LIFO, "Last in First Out). Para adicionar um item ao topo da pilha, use append(). Para recuperar um item do topo da pilha use pop() sem nenhum índice.

```python
a.append(10)
```

```python
a.pop()
```

* Comando ```del```
Uma outra forma de remover um item de uma lista conhecendo apenas seu índice, ao invés de seu valor é utilizando o comando ```del```.

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```
* Tamanho da lista
Usando a função ```len``` teremos como retorno o número de elementos de nossa lista.

```python
>>> lista = [ 1, 2, 3 ]
>>> len(lista)
3
>>> l = []
>>> len(l)
0
```

* Usando o ```range```
A função range com certeza será de grande ajuda em algum momento da sua vida. Basicamente, ela pode gerar listas simples de forma mais simples ainda.

```python
for num in range(10):
    print (num)
```
Ainda é possível passar um terceiro argumento, que será o intervalor do salto entre cada número gerado. Por exemplo:
```python
for num in range(0, 20, 2):
    print (num)
```