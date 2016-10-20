#Estrutura de Dados: Fila
#FIFO: First In, First Out


class Fila:
    def __init__(self): # Construtor da classe
        self.fila = []
    def __repr__(self): # Retorna uma representação visual do objeto
        return self.fila.__repr__()
    def tamanho(self): # Retorna o tamanho da fila
        return len(self.fila)
    def adicionar(self, n): # Adiciona itens no fim da fila
        self.fila.append(n)
    def remover(self): # Remove itens do início da fila caso ela não esteja vazia
        if self.tamanho() != 0:
            del self.fila[0]
