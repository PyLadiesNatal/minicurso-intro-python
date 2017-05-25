# Funções

As funções são úteis para empacotas uma tarefa espacífica em um trecho de código. A vontagem disso é a reutilização do código, a solução criada naquelafunção poderá ser usada sempre que necessária sem precisar que reescreve-la sempre.

Para definir novas funções devemos usar a instrução def, como no exemplo a baixo:

```
>>> def soma(a,b):
...     print(a + b)
...
>>> soma(5, 5)
10
```

Nós ainda podemos definir um retorno para a função, modificando a função da soma, vamos colocá-la para retornar o valor resultante.
```
>>> def soma(a,b):
...     return(a + b)
...
>>> print(soma(5, 5))
10
```

** Funções como parâmetros
Uma possibilidade que existe em Python é fazer a passagem de funções como parâmetros. Assim, será possível combinar várias funções para realizar uma tarefa.
```
def soma(a, b):
    return a+b
def subtracao(a, b):
    return a-b
def imprime(a, b, foper):
    print(foper(a,b))
imprime(5, 4, soma)
imprime(10, 1, subtracao)
```

** Empacotamento e desempacotamento de parâmetros
```
def soma(a, b):
    print(a+b)
L = [2, 3]
soma(*L)
```

Quando fazemos a chamada da função soma, passamos *L, esse asterisco irá indicar que queremos desempacotar a lista L utilizando seus valores como parâmetro para a função soma. No nosso exemplo L[0] será atribuido a a e L[1] será atribuido a b.

** Função Lambda
Podemos criar funções semples, sem nome, chamadas de função lambda.
```
a = lambda z: x* 2
print(a(3))
```