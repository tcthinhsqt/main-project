from flask                         import Flask, request, flash, jsonify, make_response
from flask_sqlalchemy              import SQLAlchemy
from flask_cors                    import CORS
from transformer.Transformer_model import Transformer_model
from datetime import datetime, date
import os
import hashlib
import re
import concurrent.futures

application = Flask(__name__)
application.config.update(SECRET_KEY = os.urandom(24))
application.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/admin'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
application.config['CORS_HEADERS'] = 'Content-Type'
CORS(application)

db    = SQLAlchemy(application)
model = Transformer_model()

class User(db.Model):
    id                = db.Column(db.Integer, primary_key = True, autoincrement = False)
    name              = db.Column(db.String(60), nullable = False)
    birthday          = db.Column(db.Date, nullable = False)
    gender            = db.Column(db.Integer, nullable = False)
    address           = db.Column(db.String(255))
    email             = db.Column(db.String(60), unique = True, nullable = False)
    password          = db.Column(db.String(100), nullable = False)
    number_access     = db.Column(db.Integer, nullable = False, default = 0)
    registration_date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    faculty           = db.Column(db.String(70))
    degree            = db.Column(db.String(20))
    validations       = db.relationship('Validation')

    def getInfo(user):
        return jsonify(
                           id                = user.id,
                           name              = user.name,
                           birthday          = user.birthday,
                           gender            = user.gender,
                           address           = user.address,
                           email             = user.email,
                           password          = user.password,
                           number_access     = user.number_access,
                           registration_date = user.registration_date,
                           faculty           = user.faculty,
                           degree            = user.degree
                       )

    def __repr__(self):
        return '<User %r>' % self.username


class Validation(db.Model):
    id            = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id       = db.Column(db.Integer, db.ForeignKey('user.id'))
    question      = db.Column(db.String(500), nullable = False)
    answer        = db.Column(db.String(2000), nullable = False)
    feedback      = db.Column(db.String(1000))
    validate_date = db.Column(db.DateTime, default=datetime.utcnow, nullable = False)
    rank          = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return '<Validation %r>' % self.rank

@application.route('/api/test', methods=['GET'])
def result1():
    users = User.query.all()
    users = [User.getInfo(user) for user in users]

    return users[1]

@application.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.form

        idExists = User.query.filter_by(id=data['id']).first() is not None
        emailExists = User.query.filter_by(email=data['email']).first() is not None

        if(idExists == True or emailExists == True):
            return jsonify(code = 403, message = 'Error: MSSV or Email was exists!!!')

        user = User(
                    id                = data['id'],
                    name              = data['name'],
                    birthday          = data['birthday'],
                    gender            = data['gender'],
                    address           = data['address'],
                    email             = data['email'],
                    password          = hashlib.md5(data['password'].encode()).hexdigest(),
                    faculty           = data['faculty'],
                    degree            = data['degree']
                    )
        db.session.add(user)
        db.session.commit()

        return jsonify(code = 200, message = 'Register successful!!!')
    except:
        return jsonify(code = 403, message = 'Register failed!!!')

@application.route('/api/login', methods=['POST'])
def login():
    try:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  #check if string is an email
        data  = request.form

        if(re.search(regex, data['username'])):
            user = User.query.filter_by(email = data['username']).first_or_404()
        else:
            user = User.query.filter_by(id = data['username']).first_or_404()

        if(user.password != hashlib.md5(data['password'].encode()).hexdigest()):
            raise Exception()

        return User.getInfo(user)
    except:
        return jsonify(code = 403, message = 'Login information does not match our records!!!')

@application.route('/api/validate', methods=['POST'])
def validate():
    try:
        data = request.form
        validation = Validation(
                                user_id  = data['user_id'],
                                question = data['question'],
                                answer   = data['answer'],
                                feedback = data['feedback'],
                                rank     = data['rank']
                               )
        db.session.add(validation)
        db.session.commit()
        return 'Validate successful!!!'
    except:
        return jsonify(code = 403, message = 'Validate failed!!!')

@application.route('/api/question', methods=['POST'])
def question():
    def do_work(question):
        # do something that takes a long time
        answer, question = model.evaluate(question)

        return answer, question
    try:
        question = str(request.get_json(silent=True)).strip()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(do_work, question)
            answer, question = future.result()
            return jsonify(answer = answer, question = question)
    except:
        return jsonify(code = 403, message = 'The question was wrong!!!')

if __name__ == "__main__":
    application.run(debug = True, host = '0.0.0.0')