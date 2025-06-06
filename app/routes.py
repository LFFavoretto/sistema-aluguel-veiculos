from app import app
from flask import render_template as rt, request

veiculos = {
    1:{"modelo":"Gol", "disponivel":True},
    2:{"modelo":"Corolla", "disponivel":True},
    3:{"modelo":"Chevrolet", "disponivel":True},
}

@app.route('/')

def index():
    return rt('index.html')

@app.route('/automóveis', method=['GET', 'POST'])

def Verificar():
    if request.method == 'POST':
        try:
            id_veiculo = int(request.form['id_veiculo'])
            veiculo = veiculos.get(id_veiculo)
            if veiculo:
                status = "Alugado" if veiculo["alugado"] else "Disponível"
                return rt('verificar.html', veiculo=veiculo, id=id_veiculo, status=status)
            else:
                erro = f"Veículo com ID {id_veiculo} não encontrado."
                return rt('verificar.html', erro=erro)
        except ValueError:
            erro = "Por favor, insira um número válido para o ID do veículo."
            return rt('verificar.html', erro=erro)
    return rt('verificar.html')





















