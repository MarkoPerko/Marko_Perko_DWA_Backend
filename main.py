from flask import Flask, Response, jsonify, request, render_template, json
from domain import Igrac, Statistika, Djelatnik, Vjezba, Inventar_, Event, Login
from model import Users
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from datetime import datetime
from pony.orm import db_session, select
from uuid import uuid4 as gid, UUID


app = Flask(__name__)


jwt = JWTManager(app)

CORS(app)

@app.route("/Eventi")
def Eventi():
    return render_template('Eventi.html') 

@app.route("/Eventi/dodaj")
def eventi_dodaj():
    return render_template('Eventi_dodaj.html')  

@app.route("/Vjezbe")
def Vjezbe():
    return render_template('Vjezbe.html') 

@app.route("/Vjezbe/dodaj")
def Vjezbe_dodaj():
    return render_template('Vjezbe_dodaj.html')  

@app.route("/Statistika")
def Statistika():
    return render_template('Statistika.html') 

@app.route("/Eventi/dodaj")
def Statistika_dodaj():
    return render_template('Statistika_dodaj.html')  

@app.route("/Igraci")
def igraci():
    return render_template('igraci.html') 

@app.route("/igraci/dodaj")
def igraci_dodaj():
    return render_template('igraci_dodaj.html')    

@app.route("/Inventar")
def inventar():
    return render_template('inventar.html') 

@app.route("/inventar/dodaj")
def inventar_dodaj():
    return render_template('inventar_dodaj.html') 

@app.route("/Djelatnici")
def djelatnici():
    return render_template('djelatnici.html')

@app.route("/djelatnici/dodaj")
def djelatnici_dodaj():
    return render_template('djelatnici_dodaj.html')     

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/igraci", methods=["GET"])
def handle_igraci():
    igraci = Igrac.listaj()
    return jsonify({"IGRAC": igraci})

@app.route("/igraci/novi", methods=["POST"])
def handle_igraci_dodaj():
    status, greske = Igrac.dodaj(request.get_json())
    if status:
        return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r

@app.route("/statistika", methods=["GET"])
def handle_statistika():
    statistika = Statistika.listaj()
    return jsonify({"statistika igraca": statistika})

@app.route("/statistika/novi", methods=["POST"])
def handle_statistika_dodaj():
    status, greske = Statistika.dodaj(request.get_json())
    if status:
        return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r


@app.route("/djelatnici", methods=["GET"])
def handle_djelatnici():
    djelatnici = Djelatnik.listaj()
    return jsonify({"djelatnik": djelatnici})

@app.route("/djelatnici/novi", methods=["POST"])
def handle_djelatnici_dodaj():
    status, greske = Djelatnik.dodaj(request.get_json())
    if status:
        return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r




@app.route("/vjezbe", methods=["GET"])
def handle_vjezbe():
    vjezbe = Vjezba.listaj()
    return jsonify({"Vjezbe": vjezbe})
    

@app.route("/vjezbe/novi", methods=["POST"])
def handle_vjezbe_dodaj():
    status, greske = Vjezba.dodaj(request.get_json())
    if status:
        return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r



@app.route("/inventar", methods=["GET"])
def handle_inventar():
    inventar = Inventar_.listaj()
    return jsonify({"inventar": inventar})

@app.route("/inventar/novi", methods=["POST"])
def handle_inventar_dodaj():
    status, greske = Inventar_.dodaj(request.get_json())
    if status:
        return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r

@app.route("/eventi", methods=["GET"])
def handle_eventi():
    eventi = Event.listaj()
    return jsonify({"event": eventi})

@app.route("/eventi/novi", methods=["POST"])
def handle_eventi_dodaj():
    status, greske = Event.dodaj(request.get_json())
    if status:
        return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r

@app.route('/user/register', methods=['POST'])
def register():
    
    status, greske = Login.dodaj(request.get_json())
    if status:
        return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r


@app.route('/user/login', methods=['POST'])
def login():
    
    status, greske = Login.prijava(request.get_json())
    print( "radim")
    if status:
        return Response(status=201)
    else:
        r = Response(status=500)
        r.set_data(greske)
        return r


if __name__=='__main__':
    app.debug = True
    app.run()



