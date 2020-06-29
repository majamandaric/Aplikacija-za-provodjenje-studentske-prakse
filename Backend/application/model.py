from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Class Poslodavac
class Poslodavac(db.Model):
    _tablename_ = "poslodavac"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    lozinka = db.Column(db.String(120))
    ime = db.Column(db.String(80))
    prezime = db.Column(db.String(80))
    naziv_poduzeca = db.Column(db.String(120), unique=True)
    oib_poduzeca = db.Column(db.Integer, unique=True)
    mjesto = db.Column(db.String(120))
    web = db.Column(db.String(120))

    projekti = db.relationship('Projekt', back_populates='poslodavac', lazy="dynamic")

    def __init__(self, **kwargs):
        super(Poslodavac, self).__init__(**kwargs)

    def serialize(self):
        return {
            'id': self.id,
            'ime': self.ime,
            'prezime': self.prezime,
            'email': self.email,
            'lozinka': self.lozinka,
            'naziv_poduzeca': self.naziv_poduzeca,
            'oib_poduzeca': self.oib_poduzeca,
            'mjesto': self.mjesto,
            'web': self.web
        }

# Class Projekt
class Projekt(db.Model):
    _tablename_ = "projekt"

    id = db.Column(db.Integer, primary_key=True)
    kontakt_osoba = db.Column(db.String(120))
    naziv_poduzeca = db.Column(db.String(120))
    zadatak_studenta = db.Column(db.String(1000))
    preferirane_tehnologije = db.Column(db.String(500))
    broj_studenta = db.Column(db.Integer)
    preferencije = db.Column(db.String(500))
    potrebna_infrastruktura = db.Column(db.String(500))
    broj_sati = db.Column(db.String(20))
    lokacija = db.Column(db.String(120))
    vrijeme_pocetka = db.Column(db.String(120))
    angazman_nastavnika = db.Column(db.String(500))
    dodatna_napomena = db.Column(db.String(500))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)

    poslodavac_id = db.Column(db.Integer, db.ForeignKey('poslodavac.id'), nullable=False)

    poslodavac = db.relationship('Poslodavac', back_populates='projekti', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'kontakt_osoba': self.kontakt_osoba,
            'naziv_poduzeca': self.naziv_poduzeca,
            'zadatak_studenta': self.zadatak_studenta,
            'preferirane_tehnologije': self.preferirane_tehnologije,
            'broj_studenta': self.broj_studenta,
            'preferencije': self.preferencije,
            'potrebna_infrastruktura': self.potrebna_infrastruktura,
            'broj_sati': self.broj_sati,
            'lokacija': self.lokacija,
            'vrijeme_pocetka': self.vrijeme_pocetka,
            'angazman_nastavnika': self.angazman_nastavnika,
            'dodatna_napomena': self.dodatna_napomena,
            'created_at': self.created_at
        }

# Class Student
class Student(db.Model):
    _tablename_ = "student"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    lozinka = db.Column(db.String(120))
    ime = db.Column(db.String(80))
    prezime = db.Column(db.String(80))
    grad = db.Column(db.String(120))
    sveuciliste = db.Column(db.String(120))
    smjer = db.Column(db.String(120))
    jmbag = db.Column(db.String(120))
    vrsta_studija = db.Column(db.String(120))
    godina = db.Column(db.String(120))

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'lozinka': self.lozinka,
            'ime': self.ime,
            'prezime': self.prezime,
            'grad': self.grad,
            'jmbag': self.jmbag,
            'vrsta_studija': self.vrsta_studija,
            'sveuciliste': self.sveuciliste,
            'smjer': self.smjer,
            'godina': self.godina
        }

# Class Profesor
class Profesor(db.Model):
    _tablename_ = "profesor"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    lozinka = db.Column(db.String(120))
    ime = db.Column(db.String(80))
    prezime = db.Column(db.String(80))

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'lozinka': self.lozinka,
            'ime': self.ime,
            'prezime': self.prezime
        }

# Class Odabir
class Odabir(db.Model):
    _tablename_ = "odabir"
    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(120))
    prezime = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    godina = db.Column(db.String(120))
    smjer = db.Column(db.String(120))
    jmbag = db.Column(db.String(120))
    vrsta_studija = db.Column(db.String(120))
    odabir1_ime_projekta = db.Column(db.String(220))
    odabir2_ime_projekta = db.Column(db.String(220))
    odabir3_ime_projekta = db.Column(db.String(220))

    def serialize(self):
        return {
            'id': self.id,
            'ime': self.ime,
            'prezime': self.prezime,
            'email': self.email,
            'godina': self.godina,
            'smjer': self.smjer,
            'jmbag': self.jmbag,
            'vrsta_studija': self.vrsta_studija,
            'odabir1_ime_projekta': self.odabir1_ime_projekta,
            'odabir2_ime_projekta': self.odabir2_ime_projekta,
            'odabir3_ime_projekta': self.odabir3_ime_projekta
        }

# Class Favoriti
class Favoriti(db.Model):
    _tablename_ = "favoriti"
    id = db.Column(db.Integer, primary_key=True)
    kontakt_osoba = db.Column(db.String(120))
    naziv_poduzeca = db.Column(db.String(120))
    zadatak_studenta = db.Column(db.String(1000))
    preferirane_tehnologije = db.Column(db.String(500))
    broj_studenta = db.Column(db.Integer)
    preferencije = db.Column(db.String(500))
    potrebna_infrastruktura = db.Column(db.String(500))
    broj_sati = db.Column(db.String(20))
    lokacija = db.Column(db.String(120))
    vrijeme_pocetka = db.Column(db.String(120))
    angazman_nastavnika = db.Column(db.String(500))
    dodatna_napomena = db.Column(db.String(500))
    student_id = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'kontakt_osoba': self.kontakt_osoba,
            'naziv_poduzeca': self.naziv_poduzeca,
            'zadatak_studenta': self.zadatak_studenta,
            'preferirane_tehnologije': self.preferirane_tehnologije,
            'broj_studenta': self.broj_studenta,
            'preferencije': self.preferencije,
            'potrebna_infrastruktura': self.potrebna_infrastruktura,
            'broj_sati': self.broj_sati,
            'lokacija': self.lokacija,
            'vrijeme_pocetka': self.vrijeme_pocetka,
            'angazman_nastavnika': self.angazman_nastavnika,
            'dodatna_napomena': self.dodatna_napomena,
            'student_id': self.student_id
        }

# Class Arhiva
class Arhiva(db.Model):
    _tablename_ = "arhiva"
    id = db.Column(db.Integer, primary_key=True)
    kontakt_osoba = db.Column(db.String(120))
    naziv_poduzeca = db.Column(db.String(120))
    zadatak_studenta = db.Column(db.String(1000))
    preferirane_tehnologije = db.Column(db.String(500))
    broj_studenta = db.Column(db.Integer)
    preferencije = db.Column(db.String(500))
    potrebna_infrastruktura = db.Column(db.String(500))
    broj_sati = db.Column(db.String(20))
    lokacija = db.Column(db.String(120))
    vrijeme_pocetka = db.Column(db.String(120))
    angazman_nastavnika = db.Column(db.String(500))
    dodatna_napomena = db.Column(db.String(500))
    poslodavac_id = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'kontakt_osoba': self.kontakt_osoba,
            'naziv_poduzeca': self.naziv_poduzeca,
            'zadatak_studenta': self.zadatak_studenta,
            'preferirane_tehnologije': self.preferirane_tehnologije,
            'broj_studenta': self.broj_studenta,
            'preferencije': self.preferencije,
            'potrebna_infrastruktura': self.potrebna_infrastruktura,
            'broj_sati': self.broj_sati,
            'lokacija': self.lokacija,
            'vrijeme_pocetka': self.vrijeme_pocetka,
            'angazman_nastavnika': self.angazman_nastavnika,
            'dodatna_napomena': self.dodatna_napomena,
            'poslodavac_id': self.poslodavac_id
        }