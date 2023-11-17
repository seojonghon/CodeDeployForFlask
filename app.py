from flask import Flask
app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'hello flask & code deploy V2'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
