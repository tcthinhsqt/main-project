from flask                         import Flask, request, flash, jsonify, make_response, abort
from flask_sqlalchemy              import SQLAlchemy
from flask_cors                    import CORS
from transformer.Transformer_model import Transformer_model
from datetime import datetime, date, timedelta
import os
import hashlib
import re
import concurrent.futures
from werkzeug.exceptions import HTTPException
import uuid
from sqlalchemy import extract

application = Flask(__name__)
application.config.update(SECRET_KEY = os.urandom(24))
application.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/admin?charset=utf8mb4'
application.config["MYSQL_DATABASE_CHARSET "] = 'utf8mb4'
application.config["MYSQL_CHARSET "] = 'utf8mb4'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
application.config['CORS_HEADERS'] = 'Content-Type'
CORS(application, resources={r"/api/*": {"origins": "*"}})

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
    remember_token    = db.Column(db.String(50))
    expired_time      = db.Column(db.DateTime)
    validations       = db.relationship('Validation')

    def getInfo(user):
        return jsonify(
                           id                = user.id,
                           name              = user.name,
                           birthday          = (user.birthday).strftime('%Y/%m/%d'),
                           gender            = user.gender,
                           address           = user.address,
                           email             = user.email,
                           password          = user.password,
                           number_access     = user.number_access,
                           registration_date = (user.registration_date).strftime('%Y/%m/%d'),
                           faculty           = user.faculty,
                           degree            = user.degree,
                           expired_time      = user.expired_time,
                           remember_token    = user.remember_token
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

    def getInfo(validator):
        return jsonify(
                           id            = validator.id,
                           user_id       = validator.user_id,
                           question      = validator.question,
                           answer        = validator.answer,
                           feedback      = validator.feedback,
                           validate_date = validator.validate_date,
                           rank          = validator.rank
                       )

    def __repr__(self):
        return '<Validation %r>' % self.rank

@application.route('/api/test', methods=['GET'])
def result1():
    users = User.query.all()
    users = [User.getInfo(user) for user in users]

    return users[1]

@application.route('/api/register', methods=['POST'])
@application.errorhandler(Exception)
def register():
    try:
        data = request.get_json(silent=True)

        idExists = User.query.filter_by(id=data['id']).first() is not None
        emailExists = User.query.filter_by(email=data['email']).first() is not None

        if(idExists == True or emailExists == True):
            return jsonify(code = 403, id = 'Error: MSSV or Email was exists!!!', email = 'Error: MSSV or Email was exists!!!'), 403

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
        return jsonify(code = 403, message = 'Register Failed!!!'), 403

@application.route('/api/update-user', methods=['POST'])
@application.errorhandler(Exception)
def updateUser():
    try:
        data = request.get_json(silent=True)

        user = User.query.filter_by(id = data['id']).first_or_404()

        if(not user):
            raise Exception()

        user.name     = data['name']
        user.birthday = data['birthday']
        user.gender   = data['gender']
        user.address  = data['address']
        user.email    = data['email']
        user.faculty  = data['faculty']
        user.degree   = data['degree']

        db.session.commit()

#         return jsonify(data = data, user = '')
        return User.getInfo(user)
    except:
        return jsonify(code = 403, message = 'Update Profile Failed!!!'), 403

@application.route('/api/change-password', methods=['POST'])
@application.errorhandler(Exception)
def changePassword():
    try:
        data = request.get_json(silent=True)
        id = request.args.get('id')

        user = User.query.filter_by(id = id).first_or_404()

        if(not user):
            raise Exception()

        if(user.password != hashlib.md5(data['password'].encode()).hexdigest()):
            return jsonify(code = 403, message = 'Sai mật khẩu!!!'), 403

        if(user.password == hashlib.md5(data['new_password'].encode()).hexdigest()):
            return jsonify(code = 403, message = 'Mật khẩu mới không thể giống với mật khẩu cũ!!!'), 403

        user.password = hashlib.md5(data['new_password'].encode()).hexdigest()

        db.session.commit()

        return jsonify(code = 200, message = 'Thay đổi mật khẩu thành công!!!')
    except:
        return jsonify(code = 403, message = 'Thay đổi mật khẩu thất bại!!!'), 403

@application.route('/api/login', methods=['POST'])
@application.errorhandler(Exception)
def login():
    try:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  #check if string is an email
        data = request.get_json(silent=True)

        if(re.search(regex, data['username'])):
            user = User.query.filter_by(email = data['username']).first_or_404()
        else:
            user = User.query.filter_by(id = data['username']).first_or_404()

        if(user.password != hashlib.md5(data['password'].encode()).hexdigest()):
            raise Exception()

        user.remember_token = str(uuid.uuid4())
        user.expired_time = datetime.now() + timedelta(hours=1)
        db.session.commit()

        return User.getInfo(user)

    except:
        return jsonify(code = 403, message = 'Login information does not match our records!!!'), 403

@application.route('/api/logout', methods=['POST'])
@application.errorhandler(Exception)
def logout():
    try:
        data = request.get_json(silent=True)

        user = User.query.filter_by(id = data['id']).first_or_404()

        if(not user):
            raise Exception()

        user.remember_token = None
        user.expired_time   = None
        db.session.commit()

        return jsonify(code = 200, message = 'Logout successful!!!'), 200

    except:
        return jsonify(code = 403, message = 'Logout Failed!!!'), 403

@application.route('/api/validate', methods=['POST'])
def validate():
    try:
        data = request.get_json(silent=True)
        id = request.args.get('id')
        user = User.query.filter_by(id = id).first()
        if(not user):
            id = None
        validation = Validation(
                                user_id  = id,
                                question = data['question'],
                                answer   = data['answer'],
                                feedback = data['feedback'],
                                rank     = data['rate']
                               )
        db.session.add(validation)
        db.session.commit()
        return jsonify(code = 200, message = 'Validate successful!!!'), 200
    except:
        return jsonify(code = 403, message = 'Validate failed!!!'), 403

@application.route('/api/question', methods=['POST'])
@application.errorhandler(Exception)
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

            id = request.args.get('id')
            if(id):
                user = User.query.filter_by(id = id).first_or_404()

                if(not user):
                     raise Exception()

                user.number_access = user.number_access + 1

                db.session.commit()


            return jsonify(answer = answer, question = question)
    except:
        return jsonify(code = 403, question = 'The question was wrong!!!'), 403

@application.route('/api/statistic', methods=['GET'])
@application.errorhandler(Exception)
def statistic():
    try:
        users = User.query.all()
        validations = Validation.query.all()
        number_validation = Validation.query.count()
        totalUse = 0
        totalRate = 0

        for i in users:
            totalUse = totalUse + i.number_access
        for i in validations:
            totalRate = totalRate + i.rank

        averageRate = round(totalRate/number_validation, 1)

        rate = []
        for i in range(1,6):
            rate.append(Validation.query.filter_by(rank = i).count())

        return jsonify(totalUse = totalUse, averageRate = averageRate, rate = rate)
    except:
        return jsonify(code = 403, question = 'The question was wrong!!!'), 403

if __name__ == "__main__":
    application.run(debug = True, host = '0.0.0.0')