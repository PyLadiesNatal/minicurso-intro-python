# Dicionários
Outra estrutura de dados muito útil no Python é o dicionário, cujo tipo é dict. É uma estrutura semelhantes as listas, mas possui propriedades de acesso diferentes. Dicionários são delimitados por chaves: {}, e contém uma lista de pares chave:valor separada por vírgulas. Eles são também chamados de “memória associativa” ou “vetor associativo” em outras linguagens.
Diferente das listas e tuplas que são indexadas por inteiros, dicionários são indexados por chaves (keys), que podem ser de qualquer tipo imutável (como strings). Tuplas também podem ser chaves se contiverem apenas strings, inteiros ou outras tuplas. Se a tupla contiver, direta ou indiretamente, qualquer valor mutável, não poderá ser chave. Listas não podem ser usadas como chaves porque podem ser modificadas in place pela atribuição em índices ou fatias, e por métodos como append() e extend() [PyDoc].
Uma forma de visualizar como dicionários funcionam é vê-los como um conjunto não ordenado de pares chave-valor. Essas chaves são únicas em uma dada instância do dicionário, caso um valor que já foi atribuído a uma chave seja usado novamente, o valor associado é alterado para um novo valor, caso não existe, o par chave:valor será adicionado no dicionário.
Veja a tabela a seguir e como ela pode ser representada como um dicionário:

| Produto | Valor |
|---------|-------|
| Banana  | 3.00  |
| Maçã    | 5.00  |
| Uva     | 8.00  |

```python
>>> mercadinho = { "Banana" : 3.00,
...                "Maçã"   : 5.00,
...                "Uva"    : 8.00 }
```

Para acessar as informações do dicionário, devemos utilizar duas chaves. Usando o exemplo que demos, para acessar o preço da banana devemos usar ```mercadinho["Banana"]```.

```python
>>> print(mercadinho["Banana"])
3.0
```

Também é possível remover um par chave:valor com o comando ```del```.

```python
>>> mercadinho
{'Uva': 8.0, 'Maçã': 5.0, 'Banana': 3.0}
>>> del(mercadinho['Banana'])
>>> mercadinho
{'Uva': 8.0, 'Maçã': 5.0}
```

 Se você armazenar um valor utilizando uma chave já presente, o antigo valor será substituído pelo novo.

```python
>>> mercadinho
{'Uva': 8.0, 'Maçã': 5.0, 'Banana': 3.0}
>>> mercadinho['Banana'] = 7.0
>>> mercadinho
{'Uva': 8.0, 'Maçã': 5.0, 'Banana': 7.0}
```

 E por último, se tentarmos recuperar um valor usando uma chave inexistente, será gerado um erro do tipo ```KeyError```. Como no exemplo:

```python
>>> mercadinho
{'Uva': 8.0, 'Maçã': 5.0, 'Banana': 3.0}
>>> print(mercadinho["Laranja"])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Laranja'
>>>
```
