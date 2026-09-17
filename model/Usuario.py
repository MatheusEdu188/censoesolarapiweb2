
class Usuario():

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome


    def __str__(self):
        return f"<Usuario: {self.cpf}, {self.nome}>"


    def to_dict(self):
        return {
            "cpf": self.cpf,
            "nome": self.nome
        }


pessoa = Pessoa("1704478984", "Joao")


print(pessoa)

