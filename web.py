import os
from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    data = [datetime().day, datetime().month, datetime().year] 
    return 'Hoje é dia: ', data[0], '/', data[1], '/', data[2], '.'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
