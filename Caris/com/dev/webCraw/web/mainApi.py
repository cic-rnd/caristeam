from flask import Flask, render_template
from flask import Flask
from flask import request

from com.dev.webCraw.service.crawService import crawService

app = Flask(__name__)


# @app.route('/', methods=['GET'])
# def home():
#     return '<h1> flask web test page </h1>'

@app.route('/', methods=['GET'])
def webCrawPage():
    return render_template('/webCraw.html')

@app.route('/craw', methods=['POST'])
def crawCont():
    _searchWorld = request.get_json()
    print('searchWord : {}'.format(_searchWorld['word']))
    _craw = crawService(_searchWorld['word'])
    code = _craw.crawler()
    return code

# main-test-Func.
if __name__ == '__main__':
    app.run(debug=True)
