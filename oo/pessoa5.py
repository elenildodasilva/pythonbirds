class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def cumprimentar (self):
        return f'olá {id(self)}'
    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

if __name__== '__main__':
    Pedro = Homem(nome='Pedro')
    Elenildo = Pessoa(Pedro, nome='Elenildo')
    print(Pessoa.cumprimentar(Elenildo))
    print(id(Elenildo))
    print(Elenildo.cumprimentar())
    print(Elenildo.nome)
    print(Elenildo.idade)
    for filho in Elenildo.filhos:
        print(filho.nome)
    Elenildo.sobrenome = 'Silva'
    del Elenildo.filhos
    Elenildo.olhos = 1
    del Elenildo.olhos
    print(Pedro.__dict__)
    print(Elenildo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(Elenildo.olhos)
    print(id(Pessoa.olhos), id(Elenildo.olhos), id(Pedro.olhos))
    print(Pessoa.metodo_estatico(), Elenildo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), Elenildo.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(Pedro, Pessoa))
    print(isinstance(Pedro, Homem))









