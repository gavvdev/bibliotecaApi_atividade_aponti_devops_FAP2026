import json

with open("data/livros.json",encoding="utf-8") as f:
    livros=json.load(f)

with open("data/alunos.json",encoding="utf-8") as f:
    alunos=json.load(f)

texto=f"""
RELATÓRIO

Livros: {len(livros)}

Alunos: {len(alunos)}
"""

with open("relatorio.txt","w",encoding="utf-8") as f:
    f.write(texto)

print("Relatório gerado.")