




from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import ListaSpesa, db
#inizializza l'app Flask
app = Flask(__name__)
#rotta principale
lista_spesa=[]


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()






@app.route('/')
def home():
    lista_spesa = ListaSpesa.query.all() #dalla classe listaSpesa richiediamo tutti i dati salvati e li mettiamo nella nostra lista
    return render_template('index.html', lista=lista_spesa)


@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        nuovo_elemento = ListaSpesa(elemento=elemento) #Qui stiamo creando un nuovo elemento passando il secondo elemento(app.py) a il primo elemento(models.py)
        db.session.add(nuovo_elemento) #aggiungiamo l'elemento alla sessione la sessione è una transizione temporanea come quella di git
        db.session.commit() #Qui con commit applichiamo tutte le modifiche dalla sessione al database
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    elemento = ListaSpesa.query.get_or_404(indice) #qui chiamamo il get in questo modo passiamo indice ad elemento ma se è vuoto restituisce l'errore 404
    db.session.delete(elemento) #togliamo dalla sessione l'elemento
    db.session.commit() #qui committiamo applicando la rimozione dell'elemento dalla sessione al database
    return redirect(url_for('home'))

@app.route('/svuota', methods=['POST'])
def svuota():
    ListaSpesa.query.delete() #metodo di Sqlachemy che elimina tutti gli elementi corrispondeti alla query quindi tutti
    db.session.commit() #Committiamo applicando le modifiche ossia la rimozione di tutti gli elementi al database
    return redirect(url_for('home'))

#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)