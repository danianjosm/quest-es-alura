#Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo 
        self.cor = cor 
        self.ano = ano 

meu_carro = Carro("Civic","vermelho", 2020)

print(meu_carro.modelo)
print(meu_carro.cor)
print(meu_carro.ano)
