 def __init__(self, *filhos, nome=None, idade=35):
      self.nome = nome
      self.idade = idade
      self.filhos = list(filhos)


    def cumprimentar (self):
        return f'olá {id(self)}'

if __name__== '__main__':
    Pedro = Pessoa(nome='Pedro')
    Elenildo = Pessoa(Pedro, nome='Elenildo')
    print(Pessoa.cumprimentar(Elenildo))
    print(id(Elenildo))
    print(Elenildo.cumprimentar)
    print(Elenildo.nome)
    print(Elenildo.idade)
    for filho in Elenildo.filhos:
        print(filho.nome)
    Elenildo.sobrenome = 'Silva'
    print(Elenildo.__dict__)
    print(Silva.__dict__)