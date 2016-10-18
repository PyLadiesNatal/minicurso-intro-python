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