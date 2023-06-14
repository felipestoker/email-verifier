from flask import Flask, render_template, request
import re
import socket
from validate_email import validate_email

app = Flask(__name__)


def verifica_email(email):
    # Verificação de formato
    regex = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.search(regex, email):
        return False

    # Verificação de DNS
    domain = email.split('@')[1]
    try:
        socket.gethostbyname(domain)
    except socket.gaierror:
        return False

    # Verificação SMTP
    try:
        v = validate_email(email)
    except ValueError:
        return False

    return True


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        emails = request.form['emails']
        emails = emails.splitlines()
        results = []
        for email in emails:
            if verifica_email(email):
                results.append(f'{email} é válido.')
            else:
                results.append(f'{email} é inválido.')
        return render_template('index.html', results=results)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
