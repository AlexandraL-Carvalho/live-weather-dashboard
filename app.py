from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('botao_start.html')

if __name__ == '__main__':
    app.run(debug=True) 