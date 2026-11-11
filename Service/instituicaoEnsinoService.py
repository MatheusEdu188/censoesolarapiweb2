from repositories.instituicoesEnsinoRepository import InstituicoesEnsinoRepository
from models.instituicaoEnsino import InstituicaoEnsino

class InstituicaoEnsinoService:

    def __init__(self):
        self.repository = InstituicoesEnsinoRepository()

    def getAll(self):
        lista = self.repository.findAll()

        return [ item.to_dict() for item in lista ]

    def getById(self, id):
        instituicao = self.repository.findByid( 
            id
        )

        return instituicao.to_dict()

    def insert(self, instituicao: InstituicaoEnsino):
        ie: InstituicaoEnsino = self.repository.insert(instituicao)
        ie_dict = ie.to_dict()
        return ie_dict

    def update(self, instituicao: InstituicaoEnsino):
        ie = self.repository.update(instituicao)
        ie_dict = ie.to_dict()
        
        return ie_dict
    
    def delete(self, instituicao: InstituicaoEnsino):
        ie = self.repository.delete(instituicao)
        
        return {"DELETE": ie.__str__()}
