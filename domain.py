from model import Igraci, Stat_igraca, Djelatnici, Vjezbe, Inventar, Eventi, Users
from pony.orm import db_session, select
from uuid import uuid4 as gid, UUID
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from datetime import date, datetime
from flask import Flask, Response, jsonify, request, render_template, json
class Login:
    
    @db_session()
    def dodaj(s):
        bcrypt = Bcrypt()
        try:
            s["id"] = str(gid())
            s["password"] = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
            s["created"] = str(datetime.utcnow())
            s = Users(**s)
            return True, None
        except Exception as e:
            return False, str(e)
            
    @db_session()
    def prijava(s):
        bcrypt = Bcrypt()
        try:
            s["username"] = request.get_json()['username']
            s["password"] = request.get_json()['password']
            user = Users.get(username = s["username"])
            if bcrypt.check_password_hash(user.password , s["password"]) :
                return True, None
        except Exception as e:
            return False, str(e)



class Igrac:
    @db_session()
    def listaj():
        # ORM upit
        q = select(s for s in Igraci)
        
        def dohvati_veze(x):
            if "stat" in x:
                x["stat"] = [Stat_igraca[y].to_dict() for y in x["stat"]]
            return x
        igrac = [dohvati_veze(s.to_dict(with_collections=True)) for s in q]
        return igrac
    
    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            if "stat" in s:
                statistika = s["stat"]
                statistika_sve = list(Stat_igraca[x] for x in stat)
                s["stat"] = statistika_sve
            score = Igraci(**s)
            return True, score.id
        except Exception as e:
            return False, str(e)

class Statistika:
    @db_session()
    def listaj():
        q = select(s for s in Stat_igraca)
        data = [x.to_dict() for x in q]
        return data

    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            s = Stat_igraca(**s)
            return True, None
        except Exception as e:
            return False, str(e)

class Djelatnik:
    @db_session()
    def listaj():
        q = select(s for s in Djelatnici)
        data = [x.to_dict() for x in q]
        return data

    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            s = Djelatnici(**s)
            return True, None
        except Exception as e:
            return False, str(e)


class Vjezba:
    @db_session()
    def listaj():
        q = select(s for s in Vjezbe)
        data = [x.to_dict() for x in q]
        return data

    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            s = Vjezbe(**s)
            return True, None
        except Exception as e:
            return False, str(e)

class Inventar_:
    @db_session()
    def listaj():
        q = select(s for s in Inventar)
        data = [x.to_dict() for x in q]
        return data

    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            s = Inventar(**s)
            return True, None
        except Exception as e:
            return False, str(e)

class Event:
    @db_session()
    def listaj():
        q = select(s for s in Eventi)
        data = [x.to_dict() for x in q]
        return data

    @db_session
    def dodaj(s):
        try:
            s["id"] = str(gid())
            s = Eventi(**s)
            return True, None
        except Exception as e:
            return False, str(e)

if __name__=='__main__':
    igraci = Igrac.listaj()
    print(igraci)
    statistika=Statistika.listaj()
    print(statistika)
    