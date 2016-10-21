# Tuplas
Vamos ver agora um novo tipo de sequência, um outro tipo de sequência padrão na linguagem: a tupla (tuple). Uma tupla consiste em uma sequência de valores separados por vírgulas, podendo ser vista como lista em Python, com a diferença de ser imutável (assim como strings).

```python
>>> t = 1, 2, 'python'
>>> t[0]
1
>>> t
(1, 2, 'python')
>>> # Podemos aninhar tuplas:
... u = t, (1, 2, 3, 4, 5)
>>> u
((1, 2, 'python'), (1, 2, 3, 4, 5))
```
Um ponto interessante é a criação de tuplas contendo 0 ou 1 itens: a sintaxe usa certos truques para acomodar estes casos. No caso das Tuplas vazias, um par de parênteses vazios é o necessário para construí-la; uma tupla unitária é construída por um único valor e uma vírgula entre parênteses (não basta colocar um único valor entre parênteses). Um pouco estranho, mas é assim que funciona:

```python
>>> vazia = ()
>>> upla = 'hello',    # aqui está a vírgula no final
>>> len(vazia)
0
>>> len(upla)
1
>>> upla
('hello',)
```

As tuplas também suportam acesso aos valores através dos índices e maior parte das operações das listas, como fatiamento. Podemos utilizá-las também com o ```for```:

```python
>>> numeros = (1, 2, 3, 4)
>>> for num in numeros:
        print (num)
```

Python também permite operações chamadas de empacotamento e desempacotamento. O empacotamento acontece como no exemplo:
```Pintln(t = 12345, 54321, 'python!'```. Os valores 12345, 54321, 'python!' são empacotados na tupla ```t```.
Também podemos criar tuplas a apartir de listas, usando a função ```tupla```.

```python
>>> l = [1, 2, 3]
>>> t = tuple(l)
>>> t
(1, 2, 3)
```

Mesmo que não possamos fazer alterações na tupla depois de criá-la, podemos concatená-las... mas saiba que isso gera novas tupla.

``` python
>>> t1 = (1, 2, 3)
>>> t2 = (4, 5, 6)
>>> t1 + t2
(1, 2, 3, 4, 5, 6)
```

**IMPORTANTE**: Tuplas podem conter objetos que podem ser alterados, mas as alterações nesses objetos não são consideradas mudanças na tupla em si, como no exemplo:

```python
>>> tupla = ("a", ["b", "c", "d"])
>>> tupla
('a', ['b', 'c', 'd'])
>>> len(tupla)
2
>>> tupla[1]
['b', 'c', 'd']
>>> tupla[1].append("e")
>>> tupla
('a', ['b', 'c', 'd', 'e'])
```
