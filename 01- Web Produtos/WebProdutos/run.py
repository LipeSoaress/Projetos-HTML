from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/validar_produto", methods=['POST'])
def validar_produto():
    nome_produto = request.form["nome_produto"]
    valor_produto = request.form["valor_produto"]
    quantidade_produto = request.form["quantidade_produto"]
    
    caminho_arquivo = 'models/produtos.txt'

    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(f"{nome_produto};{valor_produto};{quantidade_produto}\n")

    return redirect("/")

@app.route("/consulta")
def consulta_produtos():
    produtos = []
    caminho_arquivo = 'models/produtos.txt'

    with open(caminho_arquivo, 'r') as arquivo:
        for produto in arquivo:
            item = produto.strip().split(';')
            produtos.append({
                'nome': item[0],
                'valor': item[1],
                'quantidade': item[2]
            })


    return render_template("consulta_produtos.html", prod=produtos)

app.run(host='127.0.0.1', port=80, debug=True)

