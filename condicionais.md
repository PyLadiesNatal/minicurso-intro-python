## E se...

Agora temos um pequeno problema: e se o nosso jogador digitar uma palavra no lugar de digitar um número? Ou então, se quisermos limitar o valor de algum atributo? Por exemplo, colocar a ```life``` do nosso personagem entre 1 e 20.

Por vezes, você vai se deparar com trechos de código que poderão ser executados ou não, para tratar isso necessitaremos de expressões lógicas para representar essas escolhas. Nesse momento, usamos os condicionais para controlar o fluxo do programa. Vamos ver um exemplo:



```python
life = input("Digite o xp: ")
if life.isnumeric() and 0 < size < 20:
    life = float(life)
else:
    print('O valor digitador precisa ser numérico e estar no intervalo de 0 a 20.')
```

A ideia por trás das condições é controlar quando um trecho do código deve ser executado ou não, você vai controlar o fluxo do seu programa. Como no exemplo dado, vamos verificar se o valor de ```life``` é numérico e se está no intervalo de 0 a 20.

Agora podemos ter um controle ainda maior, e não somente 'se for verdade' e 'se não for'. 

```python
if size.isnumeric():
    size = float(size)
    if 0 < size <= 3:
        height = "short"
    elif 3 < size <= 7:
        height = "medium"
    else:
        height = "tall"
else:
    print('O valor digitado precisa ser numérico e estar no intervalo de 1 a 10.')
``` 
