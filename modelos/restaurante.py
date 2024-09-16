# Definindo a classe Restaurante
class Restaurante:
    def __init__(self, nome, categoria):
        # Inicializa o objeto com nome e categoria fornecidos
        self.nome = nome
        self.categoria = categoria
        self.ativo = False # Atributo adicional que começa como False

# Criando instâncias da classe Restaurante
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

# Criando uma lista de restaurantes
restaurantes = [restaurante_praca, restaurante_pizza]

# Imprimindo os atributos dos objetos usando vars()
print(vars(restaurante_praca))
print(vars(restaurante_pizza))
