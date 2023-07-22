import sqlite3
from flask import Flask, jsonify




app = Flask(__name__)

def conexao_banco():
    conexao = sqlite3.connect('usuarios.db')
    return conexao.cursor()

@app.route('/')
def index():
    return "Pagina inicial de teste da API, \npara ver os usuarios registrados, \nensira /usuarios no final da URL"


@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    cursor = conexao_banco()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    usuarios_organizados = []
    for usuario in usuarios:
        usuario_organizado = {
            'id': usuario[0],
            'nome': usuario[1],
            'sobrenome': usuario[2],
            'idade': usuario[3],
        }
        usuarios_organizados.append(usuario_organizado)

    return jsonify(usuarios_organizados)


@app.route('/usuarios/<int:usuario_id>', methods=['GET'])
def obter_usuarios(usuario_id):

    cursor = conexao_banco()
    cursor.execute("SELECT nome, idade, sobrenome, id FROM usuarios WHERE id = ?", (usuario_id,))
    usuario = cursor.fetchall()

    if usuario:
        
        usuario_organizado = {
            'id': usuario[0],
            'nome': usuario[1],
            'sobrenome': usuario[2],
            'idade': usuario[3],
            
            
        }
        return jsonify(usuario_organizado)
    else:
        return jsonify({"mensagem": "Usuário não encontrado"}), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)