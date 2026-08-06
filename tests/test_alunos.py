from app import app


def test_listar_alunos():

    client=app.test_client()

    resposta=client.get("/alunos")

    assert resposta.status_code==200