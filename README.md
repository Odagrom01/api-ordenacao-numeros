# API de Ordenação de Números

Esta é uma API RESTful desenvolvida com Flask para receber uma lista de números via POST, 
ordená-los em ordem crescente e armazenar o histórico de requisições em banco de dados SQLite.

---

## Tecnologias Utilizadas

- Python 3.12.5
- Flask
- Flask-SQLAlchemy
- SQLite (banco local)
- JSON

---

## Como Executar

### Opção 1: A partir do arquivo ZIP (recomendado)

1. Extraia o conteúdo do arquivo ZIP enviado por e-mail.

2. No terminal, acesse a pasta extraída:
```bash
cd nome-da-pasta-extraida
```

3. Crie um ambiente virtual e ative:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Execute a aplicação:
```bash
python main.py
```

A API estará disponível em: http://127.0.0.1:5000

### Opção 2:  Clonando via Git

1. Clone o repositório:
```bash
git clone https://github.com/Odagrom01/api-ordenacao-numeros.git
cd nome-do-projeto
```

2. Crie um ambiente virtual e ative:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute a aplicação:
```bash
python main.py
```

A API estará disponível em: http://127.0.0.1:5000

---

## Endpoints

### POST /ordenar
Ordena uma lista de números enviada no corpo da requisição.

Requisição: 
```json
{
"numeros": [5, 1, 9, 3]
}
```

Resposta:
```json
{
  "status": "ok",
  "mensagem": "Dados recebidos e armazenados com sucesso",
  "numeros_ordenados": [1, 3, 5, 9]
}
```

### GET /numeros
Retorna o histórico de listas ordenadas.

Resposta:
```json
{
  "status": "ok",
  "message": "Historico de numeros ordenados",
  "data": [
    {
      "id": 1,
      "numeros_originais": [9, 2, 4],
      "numeros_ordenados": [2, 4, 9],
      "data_criacao": "2025-05-05T15:12:34"
    }
  ],
  "total": 1
}
```

---

## Regras de Validação

1. O corpo da requisição deve conter a chave "numeros" com uma lista de pelo menos 3 números.

2. Todos os itens devem ser do tipo numérico (int ou float).

3. Caso contrário, será retornado um erro.

---

## Testes

Este projeto utiliza **pytest** para testes automatizados.

### Como executar os testes

1. Certifique-se de estar no ambiente virtual e com as dependências instaladas.

2. Execute um dos seguintes comandos no terminal, conforme seu sistema operacional:

Para Windows:
```bash
pytest .\test_api.py -v
```

Para Linux/macOS:
```bash
pytest test_api.py -v
```

Isso irá rodar todos os testes definidos no arquivo test_api.py.

### Os testes cobrem:

- Ordenação correta de listas

- Validação de dados (mínimo de 3 números)

- Resposta a dados inválidos

- Histórico de requisições

- Números com ponto flutuante

##  Exemplo de Saída dos Testes
```bash
============================= test session starts =============================
test_api.py::test_ordenacao_post PASSED                                [ 20%]
test_api.py::test_get_historico PASSED                                 [ 40%]
test_api.py::test_validacao_dados PASSED                               [ 60%]
test_api.py::test_ordenacao_decimais PASSED                            [ 80%]
test_api.py::test_erro_dados_invalidos PASSED                          [100%]
```

---

## Banco de Dados

A API utiliza um banco SQLite chamado numeros.db, criado automaticamente ao iniciar o projeto.

---

## Autor

Crystian Fonseca Morgado