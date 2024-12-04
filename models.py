from flask_sqlalchemy import SQLAlchemy #qui importiamo la classe SQLAlchemy
db = SQLAlchemy() #Creamo un oggetto di tipo SQLAlchemy
class ListaSpesa(db.Model):#definiamo una classe ListaSpesa che ha variabili di input db.Model in modo che trattera questa classe come un entità del database
    id = db.Column(db.Integer, primary_key=True) #stiamo dicecendo che id sia una colonna di db di tipo integer ed è una chiave primaria ossia un identificativo
    elemento = db.Column(db.String(100), nullable=False) #stiamo dicendo che elemento sia una collonna di tipo stringa di massimo 100 caratteri e con nullable false diciamo che sia obbligatoria


