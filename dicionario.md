## Não é o Aurélio não heim...

Outra estrutura de dados muito útil embutida em Python é o dicionário, cujo tipo é dict. É uma estrutura parecida com a lista, mas possui propriedades de acesso diferentes. Dicionários são delimitados por chaves: {} e contém uma lista de pares chave:valor separada por vírgulas. Eles são também chamados de “memória associativa” ou “vetor associativo” em outras linguagens.

**Diferente das listas, tuplas, e outras sequências indexadas por inteiros, dicionários são indexados por chaves (keys), que podem ser de qualquer tipo imutável (como strings)**

```python
mercadinho = {	"Banana" : 3.00,
				"Maçã"	 : 5.00,
				"Uva"	 : 8.00 }
```

| Produto | Valor |
|---------|-------|
| Banana  | 3.00  |
| Maçã    | 5.00  |
| Uva     | 8.00  |

Para acessar as informações do dicionário, devemos utilizar duas chaves.

```python
mercadinho["Banana"]
```
Também é possível remover um par chave:valor com o comando ```del```.

```python
del mercadinho['Banana']
```

Se você armazenar um valor utilizando uma chave já presente, o antigo valor será substituído pelo novo.

```python
mercadinho ={ "Banana" : 3.50}
```

Se tentar recuperar um valor usando uma chave inexistente, será gerado um erro do tipo ```KeyError```.

```python
>>> print(mercadinho["Manga"])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Manga'
>>>
```

Se quiser verificar se existe a chave existe no dicionário, use o operador ```in```:

```python
>>> print("Manga" in mercadinho)
False
>>> print("Uva" in mercadinho)
True
```
Dois métodos também muito importantes são o ```keys()``` e o ```values()```. O ```keys()``` devolve a lista de todas as chaves presentes no dicionário, em ordem arbitrária (se desejar ordená-las basta aplicar a função ```sorted()``` à lista devolvida). Já o ```values()``` irá retornar os valores do dicionários. O retorno de ambos os métodos são geradores, então você pode usá-los dentro de um ```for``` ou transformá-lo em lista com a função ```list```.

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'sape': 4139, 'guido': 4127, 'jack': 4098}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'guido': 4127, 'irv': 4127, 'jack': 4098}
>>> tel.keys()
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
```

O construtor dict() produz dicionários diretamente a partir de uma lista de chaves-valores, armazenadas como duplas (tuplas de 2 elementos). Quando os pares formam um padrão, uma list comprehensions pode especificar a lista de chaves-valores de forma mais compacta.

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'jack': 4098, 'guido': 4127}
>>> dict([(x, x**2) for x in (2, 4, 6)])     # use uma list comprehension
{2: 4, 4: 16, 6: 36}
```

Quando chaves são strings simples, é mais fácil especificar os pares usando argumentos nomeados no construtor:

```python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'jack': 4098, 'guido': 4127}
```

**DICA**: Caso você tenha ficado em dúvida em que situação usar dicionários ou listas, aqui vai uma dica. Se seus dados não precisam ser acessados de uma só vez, e se você normalmente usa chaves acessá-los... um dicionário seria mais interessante. Um outro ponto é a possibilidade de acessar valores através de uma chave rapidamente sem precisar fazer pesquisas, a implementação interna do docionário permite uma boa velocidade de acesso quando temos muitas chaves. Porém se você quiser manter a ordem de inserção, use listas. O dicionário não organizar as chaves, ou seja, quando você insere a primeira chave, não significa que ela manterá a posição de primeira quando você adicionar outras.
