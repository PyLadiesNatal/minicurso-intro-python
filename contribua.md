## guia de contribuição

- Caso você tenha acesso ao repositorio como contribuidora

1. Clone o repositório:
```
    $ git clone https://github.com/I-am-Gabi/minicurso-intro-python.git
```  
2. Crie uma branch com o nome relacionado ao que você vai implementar, ex: documentacao_codigo, refatorar_metodos, etc.
```
    $ git checkout -b nome_branch
```
    Ex: $ git checkout -b documentacao_codigo
    
3. Esse comando vai criar a branch e já coloca você nela, então pode começar a fazer as modificações o/

4. Terminou? Adicione:
```
    $ git add <nome dos arquivos>
```   
    Caso você queira adicionar todos os arquivos do diretorio, pode fazer:
```    
    $ git add .
```    
5. Agora basta fazer o commit. No repositório temos um bot que vai analizar as msgs de commit para que todas sejam padronizadas.
O commit vai ter composto por um subject, que seraá o titulo, e um corpo. As regras sao somente para o titulo, é necessario usar um prefixo nele... como assim:
você deve escolher uma tag ("feat", "fix", "docs", "refactor", "algo"), e adicionar uma palavra chave relacionada ao que vc fez, por exemplo:
```
    $ git commit -m "docs(readme): corrigindo erros no readme"
```   
Ou ainda:
```    
    $ git commit -m "algo(condicionais): adicionando condicionais ao codigo"
```    
Nesse caso você esta criando um commit somente com titulo, mas é possivel adicionar um corpor, com uma melhor descriçao do que foi feito, ou caso você 
tenha adicionado ou modificado algo além do que foi descrito no titulo. Uma opçao é fazer:
```
    $ git commit -a 
```

Esse comando vai abrir o editor no seu terminal.   

