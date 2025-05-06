from flask import jsonify, make_response

class Tratamentos():
    def erro_resposta(mensagem, status=400):
        return make_response(jsonify({
            'status': 'error',
            'mensagem': mensagem,
        }), status)

    def sucesso_resposta(mensagem, dados):
        return make_response(jsonify({
            'status': 'ok',
            'mensagem': mensagem,
            'numeros_ordenados': dados,
            'ordenado_formatado': f'{dados}',
        }), 200)
