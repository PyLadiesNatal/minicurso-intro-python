## guia de contribuição

- Caso você tenha acesso ao repositório como contribuidora

1. Clone o repositório:
```
    $ git clone https://github.com/I-am-Gabi/minicurso-intro-python.git
```  
2. Crie um branch com o nome relacionado ao que você vai implementar, ex: documentacao_codigo, refatorar_metodos, etc.
```
    $ git checkout -b nome_branch
```
    Ex: ```$ git checkout -b documentacao_codigo```
    
3. Esse comando vai criar o branch e já coloca você nele, então pode começar a fazer as modificações o/

4. Terminou? Adicione:
```
    $ git add <nome dos arquivos>
```   
    Caso você queira adicionar todos os arquivos do diretorio, pode fazer:
```    
    $ git add .
```    
5. Agora basta fazer o commit. No repositório, temos um bot que vai analizar as mensagens de commit para que todas sejam padronizadas.
O commit vai ter composto por um subject, que será o titulo, e um corpo. As regras são somente para o titulo, é necessario usar um prefixo nele.
Você deve escolher uma tag ("feat", "fix", "docs", "refactor", "algo"), e adicionar uma palavra-chave relacionada ao que você fez, por exemplo:
```
    $ git commit -m "docs(readme): corrigindo erros no readme"
```   
Ou ainda:
```    
    $ git commit -m "algo(condicionais): adicionando condicionais ao codigo"
```    
Nesse caso, você está criando um commit somente com titulo, mas é possivel adicionar um corpo, com uma melhor descrição do que foi feito, ou caso você 
tenha adicionado ou modificado algo além do que foi descrito no titulo. Uma opçao é fazer:
```
    $ git commit -a 
```
Esse comando vai abrir o editor no seu terminal. 

![Editor da mensagem de commit](/images/tela_commit.png)

A primeira linha é reservada ao título do commit, dando enter você pode adicionar uma mensagem de corpo.

![Editor da mensagem de commit](/images/tela_msg_commit.png)

6. Estamos quase lá, agora você pode fazer o push para a branch em que está trabalhando.

```    
    $ git push origin nome_branch
```  

7. Até agora, você subiu suas modificaçoes para seu branch no repositorio. Imagine que você esta fazendo um relatorio, e cada um precisa escrever uma pagina sobre um assunto. Você leva sua folha para casa, escreve sobre e no outro diz traz a folha de volta. Você e seus amigos se sentam e comparam o que rolou em cada folha, o que cada um fez, o que juntar, o que ficou repetido, etc...
Basicamente a branch é sua folha. Agora devemos partir para a parte de juntar o que foi escrito. Você fara o pull request o/

Uma opçao é abrir o repositorio no github, ir na aba 'Pull requests' e clicar no botao verde grandao no canto direito, 'New pull request'.

![Fazendo pull request](/images/pull_request.png)

Você vai ser encaminhada a uma pagina onde vai escolher a branch para onde vai enviar as suas modificaçoes (master), e a branch onde esta suas modificaçoes.

![Fazendo pull request](/images/pull_request_final.png)

8. Agora é esperar uma das meninas verem o que foi enviado, e dar um approves :)
