
from flask import Flask, request
from model.InstituicoesEnsino import InstituicoesEnsino
from model.Usuario import Usuario
import json

print("Iniciando a aplicação...")

app = Flask(__name__)


@app.route("/")
def index():
    return {"versão":"0.0.1"}




def carregarDados():
    with open("censoescolarapi/db.json", "r") as f:
        dados = json.load(f)

    return dados["instituicoesEnsino"]




def salvarDados(dados):
    with open("censoescolarapi/db.json", "r") as f:
        arquivo = json.load(f)

    arquivo["instituicoesEnsino"] = dados

    with open("censoescolarapi/db.json", "w") as f:
        json.dump(arquivo, f, indent=4)




instituicoesEnsino = carregarDados()



def criarInstituicao(dados):
    return InstituicoesEnsino(
        dados["id"],
        dados["no_entidade"],
        dados["co_entidade"],
        dados["no_uf"],
        dados["sg_uf"],
        dados["co_uf"],
        dados["no_municipio"],
        dados["co_municipio"],
        dados["no_mesorregiao"],
        dados["co_mesorregiao"],
        dados["no_microrregiao"],
        dados["co_microrregiao"],
        dados["nu_ano_censo"],
        dados["no_regiao"],
        dados["co_regiao"],
        dados["qt_mat_bas"],
        dados["qt_mat_inf"],
        dados["qt_mat_fund"],
        dados["qt_mat_med"],
        dados["qt_mat_prof"],
        dados["qt_mat_eja"],
        dados["qt_mat_esp"]
    )



instituto = criarInstituicao(instituicoesEnsino[0])


print(instituto)



@app.get("/instituicoesensino")
def getIntituicoes():
    return instituicoesEnsino, 200



"""@app.get("/instituicoesensinoo")
def getInstituicoesEnsino():
    coEntidade = request.args.get("co_entidade")
    for instituicao in instituicoesEnsino:
        if str(instituicao["co_entidade"])==coEntidade:
            return instituicao, 200
    return instituicoesEnsino, 200
"""


@app.get("/instituicoesensino/<int:id>")
def getByIdInstituicoes(id):

    for instituicao in instituicoesEnsino:

        if instituicao["id"] == id:
            return instituicao, 200

    return {"error": "Not found"}, 404


@app.post("/instituicoesensino")
def postInstituicoes():
    data = request.get_json()

    instituto = criarInstituicao(data)

    dadosInstituto = instituto.to_dict()

    instituicoesEnsino.append(dadosInstituto)

    salvarDados(instituicoesEnsino)

    print(dadosInstituto)

    return dadosInstituto   , 201





@app.put("/instituicoesensino/<int:id>")
def putInstituicao(id):

    data = request.get_json()

    for i, instituicao in enumerate(instituicoesEnsino):

        if instituicao["id"] == id:

            instituicaoAtualizada = criarInstituicao(data)

            instituicoesEnsino[i] = instituicaoAtualizada.to_dict()

            salvarDados(instituicoesEnsino)

            return instituicoesEnsino[i], 200

    return {"error": "Not found"}, 404






@app.delete("/instituicoesensino/<int:id>")
def deleteInstituicao(id):

    for i, instituicao in enumerate(instituicoesEnsino):

        if instituicao["id"] == id:

            instituicaoRemovida = instituicoesEnsino.pop(i)

            salvarDados(instituicoesEnsino)

            return instituicaoRemovida, 200

    return {"error": "Not found"}, 404









#Separação entre Instituições e usuario






def carregarUsuarios():
    with open("censoescolarapi/usuarios.json", "r") as f:
        dados = json.load(f)

    return dados["usuarios"]


def salvarUsuarios(dados):
    with open("censoescolarapi/usuarios.json", "r") as f:
        arquivo = json.load(f)

    arquivo["usuarios"] = dados

    with open("censoescolarapi/usuarios.json", "w") as f:
        json.dump(arquivo, f, indent=4)


usuarios = carregarUsuarios()


@app.get("/usuarios")
def getUsuarios():
    return usuarios, 200


@app.get("/usuarios/<cpf>")
def getUsuarioByCpf(cpf):

    for usuario in usuarios:

        if usuario["cpf"] == cpf:
            return usuario, 200

    return {"error": "Not found"}, 404


@app.post("/usuarios")
def postUsuario():

    data = request.get_json()

    usuario = Usuario(
        data["cpf"],
        data["nome"]
    )

    dadosUsuario = usuario.to_dict()

    usuarios.append(dadosUsuario)

    salvarUsuarios(usuarios)

    return dadosUsuario, 201


@app.put("/usuarios/<cpf>")
def putUsuario(cpf):

    data = request.get_json()

    for i, usuario in enumerate(usuarios):

        if usuario["cpf"] == cpf:

            usuarioAtualizado = Usuario(
                cpf,
                data["nome"]
            )

            usuarios[i] = usuarioAtualizado.to_dict()

            salvarUsuarios(usuarios)

            return usuarios[i], 200

    return {"error": "Not found"}, 404


@app.delete("/usuarios/<cpf>")
def deleteUsuario(cpf):

    for i, usuario in enumerate(usuarios):

        if usuario["cpf"] == cpf:

            usuarioRemovido = usuarios.pop(i)

            salvarUsuarios(usuarios)

            return usuarioRemovido, 200

    return {"error": "Not found"}, 404



















if __name__ == "__main__":
    app.run(debug=True)