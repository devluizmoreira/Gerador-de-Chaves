from flask import Flask, render_template, request, flash
import pyperclip

app = Flask(__name__)
app.secret_key = 'chave_secreta'  # Chave secreta para flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar-chave', methods=['POST'])
def gerar_chave():
    if request.method == 'POST':
        loja_codigo = request.form['loja']
        cpf = request.form['cpf']
        data = request.form['data']
        hora = request.form['hora']
        adesao = request.form['adesao']

        # Mapeamento de código para nome e código da loja
        if loja_codigo == '1':
            nome_loja = 'Grupo Cred'
            codigo_loja = '7897'
        elif loja_codigo == '2':
            nome_loja = 'Safin'
            codigo_loja = '7897'  # ou outro código correto
        elif loja_codigo == '3':
            nome_loja = 'Xinova'
            codigo_loja = '34312'
        else:
            flash("Loja inválida!", 'error')
            return render_template('index.html')

        # Validar adesao como numérico e com 8 dígitos
        if not adesao.isdigit() or len(adesao) != 8:
            flash("Adesão inválida! Deve conter 8 dígitos numéricos.", 'error')
            return render_template('index.html')

        # Construir a chave conforme o padrão
        chave = f"SEG_{codigo_loja}_{cpf}_{data}_{hora}_1_1_{adesao}"

        # Copiar chave para área de transferência
        pyperclip.copy(chave)

        flash("Chave gerada com sucesso e copiada para a área de transferência!", 'success')

        return render_template('chave.html', chave=chave, nome_loja=nome_loja)

if __name__ == '__main__':
    app.run(debug=True)
