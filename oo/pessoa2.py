class Pessoa:
    def __init__(self, nome=None):
      self.nome = nome
    def cumprimentar(self):
        return f'olá {id(self)}'

if __name__== '__main__':
    p=Pessoa('Elenildo')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome='Elenildo'
    print(p.nome)
