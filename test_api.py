import pytest
from app import app
from models import Numero
from database import db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_ordenacao_post(client):
    response = client.post(
        '/ordenar',
        json={"numeros": [3, 1, 2]},
        content_type='application/json'
    )
    
    assert response.status_code == 200
    assert response.json['status'] == 'ok'
    assert response.json['numeros_ordenados'] == [1, 2, 3]

def test_get_historico(client):
    client.post('/ordenar', json={"numeros": [5, 3, 4]})
    
    response = client.get('/numeros')
    
    assert response.status_code == 200
    assert len(response.json['data']) == 1
    assert '[3, 4, 5]' in response.json['data'][0]['numeros_ordenados']

def test_validacao_dados(client):
    response = client.post('/ordenar', json={"numeros": [1]})
    assert response.status_code == 400
    assert 'pelo menos 3 numeros' in response.json['mensagem']

def test_ordenacao_decimais(client):
    response = client.post('/ordenar', json={"numeros": [3.5, 1.2, 2.8]})
    assert response.json['numeros_ordenados'] == [1.2, 2.8, 3.5]

def test_erro_dados_invalidos(client):
    response = client.post('/ordenar', json={"numeros": "não é lista"})
    assert response.status_code == 400