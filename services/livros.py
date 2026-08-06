import json

from flask import Blueprint
from flask import jsonify
from flask import request

livros_bp = Blueprint("livros", __name__)

ARQUIVO="data/livros.json"


def ler():

    with open(ARQUIVO,"r",encoding="utf-8") as f:
        return json.load(f)


def salvar(dados):

    with open(ARQUIVO,"w",encoding="utf-8") as f:
        json.dump(dados,f,indent=4,ensure_ascii=False)


@livros_bp.get("/livros")
def listar():

    return jsonify(ler())


@livros_bp.post("/livros")
def adicionar():

    livros=ler()

    novo=request.json

    novo["id"]=len(livros)+1

    livros.append(novo)

    salvar(livros)

    return novo,201