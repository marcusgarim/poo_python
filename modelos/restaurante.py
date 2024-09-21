# Definindo a classe Restaurante
class Restaurante:
    restaurantes = []                           # Lista que irá armazenar todas as instâncias de restaurantes criadas
  
    
    def __init__(self, nome, categoria):        # Método especial de inicialização (__init__) chamado sempre que um novo objeto da classe Restaurante for criado
        self._nome = nome.title()               # Função que mantém a primeira letra maiúscula 
        self._categoria = categoria             # Atributos 'nome' e 'categoria' do restaurante
        self._ativo = False                     # Atributo '_ativo' que indica se o restaurante está aberto ou fechado (começa como False, ou seja, fechado)
        Restaurante.restaurantes.append(self)   # Adiciona a nova instância do restaurante à lista de restaurantes da classe

    
    def __str__(self):                                                      # Método especial __str__ que define a representação em string de um objeto da classe
        return f'{self._nome} | {self.categoria}'                           # Retorna o nome e a categoria do restaurante formatados

    
    @classmethod
    # Método da classe (sem o "self" pois ele atua na classe, não nas instâncias) que lista todos os restaurantes criados
    def listar_restaurantes(cls):
        print(f'{'NOME'.ljust(25)} | {'CATEGORIA'.ljust(25)} | {'STATUS'}') # Cabeçalho da tabela com nome, categoria e status dos restaurantes
        for restaurante in cls.restaurantes:                        # Para cada restaurante na lista de restaurantes, imprime as informações formatadas
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    
    @property                                                               # Propriedade que define o comportamento do atributo 'ativo' (o decorador @property para acessar o valor de _ativo como uma propriedade.). 
    def ativo(self):
        return 'Aberto' if self._ativo else 'Fechado'                       # Retorna 'Aberto' se _ativo for True, caso contrário, 'Fechado'
    

    def alternar_estado(self):
        self._ativo = not self._ativo


# Criando instâncias da classe Restaurante
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza', 'Italiana')


# Chamando o método que lista todos os restaurantes
Restaurante.listar_restaurantes()
