html="""
<h1>Biblioteca API</h1>

<p>Documentação gerada automaticamente.</p>
"""

with open("docs/api.html","w",encoding="utf-8") as f:
    f.write(html)

print("Documentação criada.")