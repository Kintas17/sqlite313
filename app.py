from flask import Flask, render_template, request

app = Flask(__name__)


def gravar(v1, v2, v3):
    import sqlite3
    ficheiro = sqlite3.connect('db/Utilizadores.db')
    db = ficheiro.cursor()
    db.execute("CREATE TABLE IF NOT EXISTS usr (usr txt, pwd txt)")
    db.execute("INSERT INTO usr VALUES (?,?)",(v1, v2) )
    ficheiro.commit()
    ficheiro.close()
    return


@app.route('/', methods=['GET', 'POST'])
def index():
    erro = None
    if request.method == 'POST':
       v1= request.form['usr']
       v2= request.form['pwd']
       v3= request.form['cpwd']
       if v2 != v3:
           erro= 'A palavra passe não coincide.'
       else:
           gravar (v1, v2, v3)
    return render_template('registo.html',erro=erro )



if __name__ == '__main__':
    app.run(debug=True)
