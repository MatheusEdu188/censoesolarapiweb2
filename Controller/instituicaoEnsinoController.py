
from flask import Blueprint, request

from models.instituicaoEnsino import InstituicaoEnsino
from services.instituicaoEnsinoService import InstituicaoEnsinoService




instituicao_bp = Blueprint("instituicao", __name__)
@instituicao_bp.get("/instituicoesEnsino")
def getAllInstituicoes():
    return InstituicaoEnsinoService().getAll(), 200





@instituicao_bp.get("/instituicoesEnsino/<int:id>")
def getByCoEntidadeInstituicoes(id):
    return InstituicaoEnsinoService().getById(id), 200







@instituicao_bp.post("/instituicoesEnsino")
def postInstituicoes():
    dados = request.json

    instituicao = InstituicaoEnsino(**dados)

    instituicao_inserida_dict = InstituicaoEnsinoService().insert(instituicao)

    return instituicao_inserida_dict, 201




@instituicao_bp.put("/instituicoesEnsino")
def putInstituicoes():
    dados = request.json

    instituicao = InstituicaoEnsino(**dados)

    return InstituicaoEnsinoService().update(instituicao), 200






@instituicao_bp.delete("/instituicoesEnsino/")
def deleteInstituicoes():
    dados = request.json

    instituicao = InstituicaoEnsino(**dados)

    return InstituicaoEnsinoService().delete(instituicao), 200
