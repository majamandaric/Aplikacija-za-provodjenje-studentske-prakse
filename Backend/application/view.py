from flask import Flask, request, jsonify, json
from flask.json import JSONEncoder
from flask_cors import CORS
from datetime import datetime
from decimal import Decimal
from .model import Poslodavac, Projekt, Student, Profesor, Odabir, Favoriti, Arhiva, db

from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(app)

def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./main_database2.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'secret'
    db.init_app(app)
    app.app_context().push()
    db.create_all()
    return app

# Home 
@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"Message": "Dobrodosli u aplikaciju Sustav za odabir studentske prakse!"})

############################################################# Poslodavac #############################################################

# Register Poslodavac
@app.route('/poslodavac/register', methods=['POST'])
def add_poslodavac():
    data = request.get_json()
    new_poslodavac = Poslodavac(email=data["email"], lozinka=data["lozinka"], ime=data["ime"], prezime=data["prezime"], naziv_poduzeca=data["naziv_poduzeca"], oib_poduzeca=data["oib_poduzeca"], mjesto=data["mjesto"], web=data["web"])
    db.session.add(new_poslodavac)
    db.session.commit()
    return jsonify(new_poslodavac)

# Login poslodavac
@app.route('/poslodavac/login', methods=['POST'])
def login_poslodavac():
    data = request.get_json()
    user = Poslodavac(email=data["email"], lozinka=data["lozinka"])
    rez = ""
    upit = Poslodavac.query.filter_by(email=user.email).first()
    upit2 = Poslodavac.query.filter_by(lozinka=user.lozinka).first()
    if upit and upit2:
        access_token = create_access_token(identity ={'id': upit.id, 'ime': upit.ime, 'prezime': upit.prezime, 'email': upit.email, 'lozinka': upit.lozinka, 'naziv_poduzeca': upit.naziv_poduzeca, 'web': upit.web})
        rez = access_token
        return rez
    else:
        rez = jsonify({"error":"Neispravana lozinka"})
        return 

# Get Poslodavaci
@app.route('/poslodavac', methods=['GET'])
def get_poslodavaci():
    poslodavac = Poslodavac.query.all()
    return jsonify(poslodavac)

# Get Single Poslodavac
@app.route('/poslodavac/<int:poslodavac_id>', methods=['GET'])
def get_poslodavac(poslodavac_id):
    poslodavac = Poslodavac.query.filter_by(id=poslodavac_id).first()
    return jsonify(poslodavac)

# Update Poslodavac
@app.route('/poslodavac/<int:poslodavac_id>', methods=['PUT'])
def update_poslodavac(poslodavac_id):
    data = request.get_json()
    poslodavac = Poslodavac.query.filter_by(id=poslodavac_id).first()

    poslodavac.email = data["email"]
    poslodavac.lozinka = data["lozinka"]
    poslodavac.ime = data["ime"]
    poslodavac.prezime = data["prezime"]
    poslodavac.naziv_poduzeca = data["naziv_poduzeca"]
    poslodavac.oib_poduzeca = data["oib_poduzeca"]
    poslodavac.mjesto = data["mjesto"]
    poslodavac.web = data["web"]

    db.session.add(poslodavac)
    db.session.commit()
    return jsonify(poslodavac)

# Delete Poslodavac
@app.route('/poslodavac/<int:poslodavac_id>', methods=['DELETE'])
def delete_poslodavac(poslodavac_id):
    poslodavac = Poslodavac.query.filter_by(id=poslodavac_id).first()
    db.session.delete(poslodavac)
    db.session.commit()
    return jsonify({})

############################################################# Poslodavac - Projekti #############################################################

# Get Poslodavac-Projekti
@app.route('/poslodavac/<int:poslodavac_id>/projekt', methods=['GET'])
def get_projekti(poslodavac_id):
    poslodavac = Poslodavac.query.filter_by(id=poslodavac_id).first()
    output = [] if poslodavac is None else poslodavac.projekti.all()
    return jsonify(output)

# Create Poslodavac-Projekt
@app.route('/poslodavac/<int:poslodavac_id>/projekt', methods=['POST'])
def add_projekt(poslodavac_id):
    data = request.get_json()
    new_projekt = Projekt(kontakt_osoba=data["kontakt_osoba"], naziv_poduzeca=data["naziv_poduzeca"], zadatak_studenta=data["zadatak_studenta"], preferirane_tehnologije=data["preferirane_tehnologije"], broj_studenta=data["broj_studenta"], preferencije=data["preferencije"], potrebna_infrastruktura=data["potrebna_infrastruktura"], lokacija=data["lokacija"], broj_sati=data["broj_sati"], vrijeme_pocetka=data["vrijeme_pocetka"], angazman_nastavnika=data["angazman_nastavnika"], dodatna_napomena=data["dodatna_napomena"], poslodavac_id=poslodavac_id)
    db.session.add(new_projekt)
    db.session.commit()
    return jsonify(new_projekt)

# Update Poslodavac-Projekt
@app.route('/poslodavac/<int:poslodavac_id>/projekt/<int:projekt_id>', methods=['PUT'])
def update_projekt(poslodavac_id, projekt_id):
    data = request.get_json()
    projekt = Projekt.query.filter_by(id=projekt_id, poslodavac_id=poslodavac_id).first()
    
    projekt.kontakt_osoba = data["kontakt_osoba"]
    projekt.naziv_poduzeca = data["naziv_poduzeca"]
    projekt.zadatak_studenta = data["zadatak_studenta"]
    projekt.preferirane_tehnologije = data["preferirane_tehnologije"]
    projekt.broj_studenta = data["broj_studenta"]
    projekt.preferencije = data["preferencije"]
    projekt.potrebna_infrastruktura = data["potrebna_infrastruktura"]
    projekt.broj_sati = data["broj_sati"]
    projekt.lokacija = data["lokacija"]
    projekt.vrijeme_pocetka = data["vrijeme_pocetka"]
    projekt.angazman_nastavnika = data["angazman_nastavnika"]
    projekt.dodatna_napomena = data["dodatna_napomena"]

    db.session.add(projekt)
    db.session.commit()
    return jsonify(projekt)

# Delete Poslodavac-Projekt
@app.route('/poslodavac/<int:poslodavac_id>/projekt/<int:projekt_id>', methods=['DELETE'])
def delete_task(poslodavac_id, projekt_id):
    projekt = Projekt.query.filter_by(id=projekt_id, poslodavac_id=poslodavac_id).first()

    db.session.delete(projekt)
    db.session.commit()
    return jsonify({})

############################################################# Student #############################################################

# Login student
@app.route('/student/login', methods=['POST'])
def login_student():
    data = request.get_json()
    user = Student(email=data["email"], lozinka=data["lozinka"])
    rez = ""
    upit = Student.query.filter_by(email=user.email).first()
    upit2 = Student.query.filter_by(lozinka=user.lozinka).first()
    if upit and upit2:
        access_token = create_access_token(identity ={'id': upit.id, 'ime': upit.ime, 'prezime': upit.prezime, 'email': upit.email, 'lozinka': upit.lozinka, 'grad': upit.grad, 'sveuciliste': upit.sveuciliste,
            'smjer': upit.smjer, 'godina': upit.godina, 'jmbag': upit.jmbag, 'vrsta_studija': upit.vrsta_studija})
        rez = access_token
        return rez
    else:
        rez = jsonify({"error":"Neispravana lozinka"})
        return 

# Get Studenti
@app.route('/student', methods=['GET'])
def get_studenti():
    student = Student.query.all()
    return jsonify(student)

# Get Single Student
@app.route('/student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.filter_by(id=student_id).first()
    return jsonify(student)

# Create Student
@app.route('/student/register', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(email=data["email"], lozinka=data["lozinka"], ime=data["ime"],
     prezime=data["prezime"], grad=data["grad"], sveuciliste=data["sveuciliste"], smjer=data["smjer"], godina=data["godina"], jmbag=data["jmbag"], vrsta_studija=data["vrsta_studija"])
    db.session.add(new_student)
    db.session.commit()
    return jsonify(new_student)

# Update Student
@app.route('/student/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    student = Student.query.filter_by(id=student_id).first()

    student.email = data["email"]
    student.lozinka = data["lozinka"]
    student.ime = data["ime"]
    student.prezime = data["prezime"]
    student.grad = data["grad"]
    student.sveuciliste = data["sveuciliste"]
    student.smjer = data["smjer"]
    student.godina = data["godina"]
    student.jmbag = data["jmbag"]
    student.vrsta_studija = data["vrsta_studija"]

    db.session.add(student)
    db.session.commit()
    return jsonify(student)

# Delete Student
@app.route('/student/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.filter_by(id=student_id).first()
    db.session.delete(student)
    db.session.commit()
    return jsonify({})

############################################################# Projekt #############################################################

# Get Projekti
@app.route('/projekt', methods=['GET'])
def get_projekt4():
    projekt = Projekt.query.all()
    return jsonify(projekt)

# Get Single Projekt
@app.route('/projekt/<int:projekt_id>', methods=['GET'])
def get_projekt3(projekt_id):
    projekt = Projekt.query.filter_by(id=projekt_id).first()
    return jsonify(projekt)

# Create Projekt
@app.route('/projekt', methods=['POST'])
def add_projekt2():
    data = request.get_json()
    new_projekt = Projekt(kontakt_osoba=data["kontakt_osoba"], naziv_poduzeca=data["naziv_poduzeca"], zadatak_studenta=data["zadatak_studenta"],
    preferirane_tehnologije=data["preferirane_tehnologije"], broj_studenta=data["broj_studenta"], preferencije=data["preferencije"],
    potrebna_infrastruktura=data["potrebna_infrastruktura"], broj_sati=data["broj_sati"], lokacija=data["lokacija"],
    vrijeme_pocetka=data["vrijeme_pocetka"], angazman_nastavnika=data["angazman_nastavnika"], dodatna_napomena=data["dodatna_napomena"], poslodavac_id=data["poslodavac_id"])
    db.session.add(new_projekt)
    db.session.commit()
    return jsonify(new_projekt)

############################################################# Profesor #############################################################

# Register Profesor
@app.route('/profesor/register', methods=['POST'])
def add_profesor():
    data = request.get_json()
    new_profesor = Profesor(email=data["email"], lozinka=bcrypt.generate_password_hash(data["lozinka"]).decode('utf-8'), ime=data["ime"], prezime=data["prezime"])
    db.session.add(new_profesor)
    db.session.commit()
    return jsonify(new_profesor)

# Login profesor
@app.route('/profesor/login', methods=['POST'])
def login_profesor():
    data = request.get_json()
    profesor = Profesor(email=data["email"], lozinka=data["lozinka"])
    rez = ""
    upit = Profesor.query.filter_by(email=profesor.email).first()
    upit2 = Profesor.query.filter_by(lozinka=profesor.lozinka).first()
    if upit and upit2:
        access_token = create_access_token(identity ={'id': upit.id, 'ime': upit.ime, 'prezime': upit.prezime, 'email': upit.email, 'lozinka': upit.lozinka})
        rez = access_token
        return rez
    else:
        rez = jsonify({"error":"Neispravana lozinka"})
        return       

# Get Profesor
@app.route('/profesor', methods=['GET'])
def get_profesor():
    profesor = Profesor.query.all()
    return jsonify(profesor)

# Get Single profesor
@app.route('/profesor/<int:profesor_id>', methods=['GET'])
def get_profesor2(profesor_id):
    profesor = Profesor.query.filter_by(id=profesor_id).first()
    return jsonify(profesor)

# Update profesor
@app.route('/profesor/<int:profesor_id>', methods=['PUT'])
def update_profesor(profesor_id):
    data = request.get_json()
    profesor = Profesor.query.filter_by(id=profesor_id).first()

    profesor.email = data["email"]
    profesor.lozinka = data["lozinka"]
    profesor.ime = data["ime"]
    profesor.prezime = data["prezime"]

    db.session.add(profesor)
    db.session.commit()
    return jsonify(profesor)

# Delete profesor
@app.route('/profesor/<int:profesor_id>', methods=['DELETE'])
def delete_profesor(profesor_id):
    profesor = Profesor.query.filter_by(id=profesor_id).first()
    db.session.delete(profesor)
    db.session.commit()
    return jsonify({})

############################################################# Odabir #############################################################

# Create Odabir
@app.route('/odabir', methods=['POST'])
def add_odabir():
    data = request.get_json()
    new_odabir = Odabir(ime=data["ime"], prezime=data["prezime"], email=data["email"],
    godina=data["godina"], smjer=data["smjer"], jmbag=data["jmbag"], vrsta_studija=data["vrsta_studija"], 
    odabir1_ime_projekta=data["odabir1_ime_projekta"], 
    odabir2_ime_projekta=data["odabir2_ime_projekta"],
    odabir3_ime_projekta=data["odabir3_ime_projekta"])
    db.session.add(new_odabir)
    db.session.commit()
    return jsonify(new_odabir)

# Get Odabir
@app.route('/odabir', methods=['GET'])
def get_odabir():
    odabir = Odabir.query.all()
    return jsonify(odabir)


############################################################# Favoriti #############################################################

# Create Favoriti
@app.route('/favoriti', methods=['POST'])
def add_favorit():
    data = request.get_json()
    new_favorit = Favoriti(kontakt_osoba=data["kontakt_osoba"], naziv_poduzeca=data["naziv_poduzeca"], zadatak_studenta=data["zadatak_studenta"],
    preferirane_tehnologije=data["preferirane_tehnologije"], broj_studenta=data["broj_studenta"], preferencije=data["preferencije"],
    potrebna_infrastruktura=data["potrebna_infrastruktura"], broj_sati=data["broj_sati"], lokacija=data["lokacija"],
    vrijeme_pocetka=data["vrijeme_pocetka"], angazman_nastavnika=data["angazman_nastavnika"], dodatna_napomena=data["dodatna_napomena"], student_id=data["student_id"])
    db.session.add(new_favorit)
    db.session.commit()
    return jsonify(new_favorit)


# Get Favoriti
@app.route('/favoriti/<int:student_id>', methods=['GET'])
def get_projekti_favoriti(student_id):
    fav = Favoriti.query.filter_by(student_id=student_id).all()
    return jsonify(fav)

#Delete Favoriti
@app.route('/favoriti/<int:favorit_id>', methods=['DELETE'])
def delete_favorit(favorit_id):
    favorit = Favoriti.query.filter_by(id=favorit_id).first()
    db.session.delete(favorit)
    db.session.commit()
    return jsonify({})

############################################################# Arhiva #############################################################

# Create Arhiva
@app.route('/arhiva', methods=['POST'])
def add_arhiva():
    data = request.get_json()
    arhiva = Arhiva(kontakt_osoba=data["kontakt_osoba"], naziv_poduzeca=data["naziv_poduzeca"], zadatak_studenta=data["zadatak_studenta"],
    preferirane_tehnologije=data["preferirane_tehnologije"], broj_studenta=data["broj_studenta"], preferencije=data["preferencije"],
    potrebna_infrastruktura=data["potrebna_infrastruktura"], broj_sati=data["broj_sati"], lokacija=data["lokacija"],
    vrijeme_pocetka=data["vrijeme_pocetka"], angazman_nastavnika=data["angazman_nastavnika"], dodatna_napomena=data["dodatna_napomena"], poslodavac_id=data["poslodavac_id"])
    db.session.add(arhiva)
    db.session.commit()
    return jsonify(arhiva)


# Get Arhiva
@app.route('/arhiva/<int:poslodavac_id>', methods=['GET'])
def get_projekti_arhiva(poslodavac_id):
    arh = Arhiva.query.filter_by(poslodavac_id=poslodavac_id).all()
    return jsonify(arh)

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):

        if hasattr(obj, "serialize"):
          return obj.serialize()

        try:
            if isinstance(obj, datetime.date) or isinstance(obj, datetime.datetime):
                return obj.isoformat()
            if isinstance(obj, Decimal):
                return str(obj)
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)

app.json_encoder = CustomJSONEncoder


if __name__ =="__main__":
  app.run(debug=True, port=8000)