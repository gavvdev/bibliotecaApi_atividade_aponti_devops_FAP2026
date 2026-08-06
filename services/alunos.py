import json

from flask import Blueprint
from flask import jsonify

alunos_bp=Blueprint("alunos",__name__)

ARQUIVO="data/alunos.json"


@alunos_bp.get("/alunos")
def listar():

    with open(ARQUIVO,"r",encoding="utf-8") as f:
        return jsonify(json.load(f))