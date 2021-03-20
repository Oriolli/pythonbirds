class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
        roger.sobrenome = 'orioli'
        del roger.filhos
        roger.olhos = 1
        del roger.olhos
        print(roger.__dict__)
        print(marcos.__dict__)
        Pessoa.olhos = 3
        print(Pessoa.olhos)
        print(roger.olhos)
        print(marcos.olhos)
        print(id(Pessoa.olhos), id(roger.olhos), id(marcos.olhos))
        print(Pessoa.metodo_estatico(), roger.metodo_estatico())
        print(Pessoa.nome_e_atributo_de_classe(), roger.nome_e_atributo_de_classe())

