class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
        marcos = Pessoa(nome='marcos')
        roger = Pessoa(marcos, nome='roger')
        print(Pessoa.cumprimentar(roger))
        print(id(roger))
        print(roger.cumprimentar())
        print(roger.nome)
        print(roger.idade)
        for filho in roger.filhos:
            print(filho.nome)