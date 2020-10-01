import os
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    data_atual = [datetime.today().day, datetime.today().month, datetime.today().year]
    frase = f'Seja muito bem vindo ao seu site no Heroku, Rodrigo. Hoje é dia {data_atual[0]}/{data_atual[1]}/{data_atual[2]}.'
    return 'Teste'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
