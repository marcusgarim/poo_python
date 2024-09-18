# Definindo a classe Restaurante
class Restaurante:
    restaurantes = []

    # Método Especial da classe  (inicializa o objeto com nome e categoria fornecidos)
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False          # Atributo adicional que começa como False
        Restaurante.restaurantes.append(self)

    # Método Especial da classe 
    def __str__(self):
        self.nome
        return f'{self.nome} | {self.categoria}'
    
    # Próprio Método
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

# Criando instâncias da classe Restaurante
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza', 'Italiana')

Restaurante.listar_restaurantes()