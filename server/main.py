from flask import Flask, render_template, request, current_app, flash, jsonify, make_response, redirect, url_for
from transformer.Transformer_model import Transformer_model
import os

application = Flask(__name__)
application.config.update(SECRET_KEY=os.urandom(24))
model = Transformer_model()

# @application.route('/about')
# def about():
#     return render_template('about.html')
#

@application.route('/api/result', methods=['POST'])
def result():
    question = str(request.form.get('input_sentence')).strip()
    if question != '':
        try:
            answer, question = model.evaluate(question)
            return jsonify(answer=answer, question=question)
        except:
          return 'Lỗi!!!'
    else:
        return 'Câu hỏi không hợp lệ!!'

if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0')