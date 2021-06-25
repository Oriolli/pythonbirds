class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}.Aperto de mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
        marcos = Mutante(nome='marcos')
        roger = Homem(marcos, nome='roger')
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
        print(Pessoa.olhos)
        print(roger.olhos)
        print(marcos.olhos)
        print(id(Pessoa.olhos), id(roger.olhos), id(marcos.olhos))
        print(Pessoa.metodo_estatico(), roger.metodo_estatico())
        print(Pessoa.nome_e_atributo_de_classe(), roger.nome_e_atributo_de_classe())
        pessoa = Pessoa('Anonimo')
        print (isinstance(pessoa, Pessoa))
        print(isinstance(pessoa, Homem))
        print(isinstance(marcos, Pessoa))
        print(isinstance(marcos, Homem))
        print(marcos.olhos)
        print(roger.cumprimentar())
        print(marcos.cumprimentar())


