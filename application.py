from flask import Flask, render_template, request
from Transformer_model import Transformer_model
import os

# S3_BUCKET                 = os.environ.get("elasticbeanstalk-us-east-2-491953769123")
# S3_KEY                    = os.environ.get("AKIAIL6QF6SBH2LN7HFQ")
# S3_SECRET                 = os.environ.get("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")

application = Flask(__name__)
# SESSION_TYPE = "redis"
# PERMANENT_SESSION_LIFETIME = 1800
application.config.update(SECRET_KEY=os.urandom(24))
model = Transformer_model()
# # application.config.from_object("config")

# s3 = boto3.client(
#                 "s3",
#                 region_name='us-east-2',
#                 aws_access_key_id=S3_KEY,
#                 aws_secret_access_key=S3_SECRET
#             )

# dynamodb = boto3.resource('dynamodb',
#                     aws_access_key_id=S3_KEY,
#                     aws_secret_access_key=S3_SECRET)

# from boto3.dynamodb.conditions import Key, Attr

# @application.route('/tfjs', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         try:
#             number = request.form['num']
#             if number == '':
#                 flash('CHƯA NHẬP KẾT QUẢ BỨC ẢNH')
#                 return render_template('tfjs.html')
                
#             file = request.form['file']

#             chuoi = file.split(',')

#             imgdata = base64.b64decode(chuoi[-1])
#             image = Image.open(io.BytesIO(imgdata))
#             img = np.array(image)
#             # img = cv2.resize(img,(28,28))
#             img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
#             (thresh, blackAndWhiteImage) = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#             images = os.listdir(f'./assets/data/{number}')
#             num = len(images)
#             cv2.imwrite(f'./assets/data/{number}/{number}_{num + 1}.jpg',blackAndWhiteImage)

#             file_name = f'assets/data/{number}/{number}_{num + 1}.jpg'
#             object_name = f'assets/data/{number}/{number}_{num + 1}.jpg'

#             region = "us-east-2"
#             bucket = "elasticbeanstalk-us-east-2-491953769123"
#             folder = f"static/data/{number}"
#             filename = f"{number}_{num + 1}.jpg"

#             s3.upload_file(file_name,bucket,object_name)  
#             url = f"https://s3.console.aws.amazon.com/s3/object/{bucket}/{folder}/{filename}?region={region}"

            
#             #DYNAMODB
#             table = dynamodb.Table('Story')
#             table.put_item(
#                     Item={
#             'link': url,
#             'result': int(number)
#                 }
#             )
#             return redirect(url_for('submit', num=number))
#         except Exception as e:
#             return "Error: {}".format(e)
        
#     else:
#         return render_template('recognition.html')

# class RegistrationForm(Form):
#     question = StringField('question', [validators.Length(min=4, max=1000),
#                                         validators.DataRequired()])
#     answer = StringField('question')




@application.route('/')
def hello_world():
    return render_template('index.html')

@application.route('/about')
def about():
    return render_template('about.html')

@application.route('/result', methods=['GET', 'POST'])
def result():
    question = str(request.form.get('input_sentence')).strip()
    if request.method=='POST' and question!='':
        try:
            answer, question = model.evaluate(question)
        except:
            return render_template('main.html', question=question, answer='Câu hỏi không hợp lệ!!')
        return render_template('main.html', question=question, answer=answer)
    else:
        return render_template('main.html')

if __name__ == "__main__":
    application.debug = True
    myPort = int(os.environ.get('PORT', 80))
    application.run(host='0.0.0.0', port=myPort, debug=True)
