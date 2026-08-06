from flask import Flask
from services.livros import livros_bp
from services.alunos import alunos_bp

app = Flask(__name__)

app.register_blueprint(livros_bp)
app.register_blueprint(alunos_bp)

@app.route("/")
def home():
    return {
        "api":"Biblioteca API",
        "versao":"1.0"
    }

if __name__ == "__main__":
    app.run(debug=True)