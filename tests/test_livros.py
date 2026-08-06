from app import app


def test_listar_livros():

    client=app.test_client()

    resposta=client.get("/livros")

    assert resposta.status_code==200