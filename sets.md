# Set
Python também inclui um tipo de dados para conjuntos, chamado set. Um conjunto é uma coleção desordenada de elementos, mas que não possui elementos repetidos. Usos comuns para sets é quando precisamos garantir que os dados não se repitam, funcionando como uma verificação eficiente da existência de objetos e a eliminação de itens duplicados. Sets também suportam operações matemáticas como união, interseção, diferença e diferença simétrica.

```python
>>> cesta = ['uva', 'laranja', 'uva', 'abacaxi', 'laranja', 'banana']
>>> frutas = set(cesta)   # criar um conjunto sem duplicatas
>>> frutas
set(['abacaxi', 'uva', 'laranja', 'banana'])
>>> 'laranja' in frutas   # testar se um elemento existe é muito rápido
True
>>> 'capim' in frutas
False
```

```python
>>> # Demonstrar operaçes de conjunto em letras únicas de duas palavras
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                # letras unicas em a
set(['a', 'r', 'b', 'c', 'd'])
>>> a - b                            # letras em a mas não em b
set(['r', 'd', 'b'])
>>> a | b                            # letras em a ou em b
set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'])
>>> a & b                            # letras tanto em a como em b
set(['a', 'c'])
>>> a ^ b                            # letras em a ou b mas não em ambos
set(['r', 'd', 'b', 'm', 'z', 'l'])
```
