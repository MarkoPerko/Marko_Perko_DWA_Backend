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

@app.route("/tablica")
def tablica():
    return render_template('tablica.html') 

@app.route("/igraci_djelatnici")
def igraci_djelatnici():
    return render_template('igraci_djelatnici.html') 

@app.route("/inventar")
def inventar():
    return render_template('inventar.html') 

@app.route("/trening")
def trening():
    return render_template('trening.html')

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/igraci", methods=["GET"])
def handle_igraci():
    igraci = Igrac.listaj()
    return jsonify({"IGRAC": igraci})

@app.route("/igraci", methods=["POST"])
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

@app.route("/statistika", methods=["POST"])
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

@app.route("/djelatnici", methods=["POST"])
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
    

@app.route("/vjezbe", methods=["POST"])
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

@app.route("/inventar", methods=["POST"])
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

@app.route("/eventi", methods=["POST"])
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



