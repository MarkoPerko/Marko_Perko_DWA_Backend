from pony.flask import Pony
from pony.orm import Database, PrimaryKey, Required, Set, db_session, Optional
from uuid import uuid4 as gid, UUID
from datetime import date, datetime
import os


db = Database()
print("tu smo")



db.bind(provider='sqlite', filename='markan.sqlite', create_db=True)


class Igraci(db.Entity):
    id = PrimaryKey(str)
    prezime = Required(str)
    ime = Required(str)
    datum = Required(date)
    registracija = Required(str, unique = True )
    stat_igraca = Optional("Stat_igraca")


class Stat_igraca(db.Entity):
    id = PrimaryKey(str)
    golovi = Optional(int)
    asistencije = Optional(int)     
    dodavanja = Optional(int)
    postotak_uspjesnih = Optional(float)
    minutaza = Optional(float)
    nastupi = Optional(int)
    crveni_kartoni = Optional(int)
    zuti_kartoni = Optional(int)
    blokovi = Optional(int)
    igraci = Required("Igraci")

class  Djelatnici(db.Entity):
    ime = Required(str)
    vrsta_djelatnika = Required(int)

class Vjezbe(db.Entity):
    id = PrimaryKey(str)
    opis = Required(str, max_len=400)
    trajanje = Required(float)
    media = Optional(str)

class Inventar(db.Entity):
    id = PrimaryKey(str)
    tip_opreme = Required(int)
    naziv = Required(str)
    kolicina = Required(int)

class Eventi(db.Entity):
    id = PrimaryKey(str)
    datum = Required(date)
    vrijeme = Required(datetime)
    opis = Optional(str, max_len = 100)
    lokacija = Required(str)

class Users(db.Entity):
    id = PrimaryKey(str)
    ime = Required(str)
    prezime = Required(str)
    username = Required(str)
    password = Required(str)
    created = Required(str)





db.generate_mapping(check_tables=True, create_tables=True)